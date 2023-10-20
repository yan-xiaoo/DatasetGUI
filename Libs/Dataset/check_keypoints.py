# check_keypoints.py
# 检查数据集中的关键点个数是否为特定值

import os
from .coco_utils import *
from .yolo_to_coco import YoloSearch
from ..process_window import ProcessFunction
from ..dataset_config import YoloDataset
from typing import Union, Optional
from pathlib import Path


class WrongAnnotation:
    def __init__(self, class_id: int, points: list[float], image_id: int = None):
        self.image_id = image_id
        self.class_id = class_id
        self.points = points

    @classmethod
    def from_annotation(cls, annotation: dict):
        return cls(annotation['category_id'], annotation['segmentation'][0], annotation['image_id'])


class WrongImage:
    def __init__(self, image_name, wrong_annotations: list[WrongAnnotation],
                 correct_keypoint_num: dict[int, int] = None, class_name: dict[int, str] = None):
        self.image_name = image_name
        self.wrong_annotations = wrong_annotations
        self.correct_keypoint_num = correct_keypoint_num
        self.class_name = class_name

    def get_wrong_message(self):
        message = [f"图片 {self.image_name} 中的关键点数量错误："]
        for annotation in self.wrong_annotations:
            if self.class_name is not None and annotation.class_id in self.class_name.keys():
                try:
                    message.append(
                        f"类别为 {self.class_name[annotation.class_id]} 的标注的关键点数量为 {int(len(annotation.points) / 2)}，应为 {self.correct_keypoint_num[annotation.class_id]}")
                except KeyError:
                    message.append(
                        f"类别为 {self.class_name[annotation.class_id]} 的标注的关键点数量为 {int(len(annotation.points) / 2)}，是错误的")
            else:
                try:
                    message.append(
                        f"类别编号为 {annotation.class_id} 的标注的关键点数量为 {int(len(annotation.points) / 2)}，应为 {self.correct_keypoint_num[annotation.class_id]}")
                except KeyError:
                    message.append(
                        f"类别编号为 {annotation.class_id} 的标注的关键点数量为 {int(len(annotation.points) / 2)}，是错误的")
        return "\n".join(message)

    def __str__(self):
        return self.get_wrong_message()


def get_yolo_classes(class_path: Union[str, Path]) -> dict[int, str]:
    """
    获取yolo数据集的类别。返回一个字典，键为类别序号，值为类别名称
    请注意：类别序号从0开始（因为yolo自己的类别序号从0开始）
    :param class_path: 类别文件路径
    :return: 类别字典
    """
    with open(class_path, 'r', encoding='utf-8') as f:
        classes = f.readlines()
    classes = [i.strip() for i in classes]
    classes = {i: classes[i] for i in range(len(classes))}
    return classes


def get_coco_keypoints(coco_file: Union[str, Path], classes: dict[int, int]) -> list[WrongImage]:
    """
    检查coco数据集中某些类的关键点个数是否为特定值
    :param coco_file: coco数据集的json文件路径
    :param classes: 每一类应当有多少个关键点。键为类别序号，值为该类的关键点个数
    请注意：类别序号从1开始（因为coco自己的类别序号从1开始）
    键也可以是类别名称，但是请注意，所有类别的名称必须是唯一的。如果有两个类别名称相同，那么会出现为定义的后果
    :return: 检查的结果列表，如果没有错误，返回空列表。
    列表内容：每个元素是一个 WrongImage 对象。
    """
    wrong_images = []
    coco = COCO(coco_file)
    class_to_name = {i['id']: i['name'] for i in coco.dataset['categories']}
    for one_annotation in coco.dataset['annotations']:
        if (one_annotation['category_id'] in classes.keys()
                and len(one_annotation['segmentation'][0]) / 2 != classes[one_annotation['category_id']]):
            for one in wrong_images:
                if one.image_name == coco.imgs[one_annotation['image_id']]['file_name']:
                    one.wrong_annotations.append(WrongAnnotation.from_annotation(one_annotation))
                    break
            else:
                wrong_images.append(WrongImage(coco.imgs[one_annotation['image_id']]['file_name'],
                                               [WrongAnnotation.from_annotation(one_annotation)],
                                               classes, class_to_name))
    return wrong_images


def get_yolo_keypoints(yolo_file: Union[str, Path], classes: dict[int, int], class_to_name: dict[int, str] = None) -> Optional[WrongImage]:
    """
    检查yolo数据集单个文件中某些类的关键点个数是否为特定值
    :param class_to_name: 用于把类别序号转换为类别名称的字典。键为类别序号，值为类别名称
    :param yolo_file: yolo数据集的txt文件路径
    :param classes:  每一类应当有多少个关键点。键为类别序号，值为该类的关键点个数
    请注意：类别序号从0开始（因为yolo自己的数据集序号从0开始）
    :return: 如果本文件中有错误，返回一个 WrongImage 对象，否则返回 None
    """
    wrong_annotations = []
    with open(yolo_file, "r", encoding='utf-8') as f:
        content = f.readlines()
    for line in content:
        line = line.strip().split()
        try:
            if int(line[0]) in classes.keys() and len(line[5:]) / 2 != classes[int(line[0])]:
                wrong_annotations.append(WrongAnnotation(int(line[0]), [float(x) for x in line[5:]]))
        except ValueError as e:
            print(e)
            print(f"文件 {yolo_file} 中的一行数据有问题：{line}")
            return None
    if wrong_annotations:
        return WrongImage(os.path.basename(yolo_file), wrong_annotations, classes, class_to_name)
    else:
        return None


class CheckYoloKeyPoints(ProcessFunction):
    def __init__(self, dataset: YoloDataset, keypoint_num, hint="正在检查关键点数量"):
        super().__init__()
        self.dataset = dataset
        self.wrong_images: list[WrongImage] = []
        self.keypoint_num = keypoint_num
        self.hint = hint
        self.class_to_name = get_yolo_classes(os.path.join(dataset.label_path, "classes.txt"))

    def run(self):
        self.setText.emit(self.hint)
        paths = [os.path.join(self.dataset.label_path, file_name) for file_name in os.listdir(self.dataset.label_path)
                 if
                 file_name.endswith(".txt") and "classes" not in file_name]
        self.setMaximum.emit(len(paths))

        for index, path in enumerate(paths):
            wrong_image = get_yolo_keypoints(path, self.keypoint_num, self.class_to_name)
            if wrong_image is not None:
                self.wrong_images.append(wrong_image)
            if not self.can_run:
                self.stopped.emit()
                break
            self.setProgress.emit(index + 1)
            self.setDetailedText.emit(f"正在检查文件 {path} {index + 1}/{len(paths)}")
        else:
            self.has_finished.emit()
