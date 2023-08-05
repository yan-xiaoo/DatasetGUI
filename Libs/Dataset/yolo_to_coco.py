import json

from PIL import Image
import os
from ..work_functions import CopyDir
from ..process_window import ProcessFunction, ProcessWindow
from ..changelog import ChangeLog


def get_classes(classes_path):
    with open(classes_path) as f:
        content = f.readlines()
    class_names = [{"id": index + 1, "name": line.strip()} for index, line in enumerate(content)]
    return class_names


def get_size(image_path):
    image = Image.open(image_path)
    size = image.size
    image.close()
    return size


def get_image(image_path, image_id):
    width, height = get_size(image_path)
    return {"id": image_id, "width": width, "height": height, "file_name": os.path.basename(image_path)}


class GetImages(ProcessFunction):
    def __init__(self, image_dir, hint="正在生成图片信息"):
        self.image_directory = image_dir
        self.images = None
        self.name_to_image_id = None
        self.hint = hint
        super().__init__()

    def run(self):
        image_paths = [os.path.join(self.image_directory, file_name) for file_name in os.listdir(self.image_directory)]
        self.images = []
        self.name_to_image_id = {}
        self.setMaximum.emit(len(image_paths))
        self.setText.emit(self.hint)
        for image_id in range(len(image_paths)):
            image_path = image_paths[image_id]
            self.name_to_image_id[os.path.basename(image_path).split('.')[0]] = image_id + 1
            self.images.append(get_image(image_path, image_id + 1))
            self.setProgress.emit(image_id + 1)
            self.setDetailedText.emit(f"正在生成图片信息 {image_id + 1}/{len(image_paths)}")
        self.has_finished.emit()


def get_annotation(label_path, name_to_image_id, annotation_id, width, height):
    # yolo_bbox
    # [x_center, y_center, w, h]
    # coco_bbox
    # [x, y, w, h]
    # x,y为box左上角的坐标
    annotations = []
    with open(label_path) as f:
        content = f.readlines()
    for line in content:
        line = line.strip().split()
        class_id = int(line[0]) + 1
        x_center = float(line[1])
        y_center = float(line[2])
        bbox_width = float(line[3])
        bbox_height = float(line[4])
        points = line[5:]
        points = list(map(float, points))
        for index, point in enumerate(points):
            points[index] = point * width if index % 2 == 0 else point * height

        bbox = [(x_center - bbox_width / 2) * width, (y_center - bbox_height / 2) * height, bbox_width * width,
                bbox_height * height]

        image_id = name_to_image_id[os.path.basename(label_path).split('.')[0]]
        annotations.append({"id": annotation_id, "iscrowd": 0, "image_id": image_id,
                            "category_id": class_id,
                            "segmentation": [points],
                            "bbox": bbox,
                            "area": bbox_width * bbox_height * width * height,
                            })
        annotation_id += 1

    return annotations


class GetAnnotations(ProcessFunction):
    def __init__(self, label_directory, image_directory, name_to_image_id, hint="正在生成标注信息"):
        self.label_directory = label_directory
        self.image_directory = image_directory
        self.name_to_image_id = name_to_image_id
        self.annotations = []
        self.search = YoloSearch(image_directory)
        self.hint = hint
        super().__init__()

    def run(self):
        annotation_id = 0
        paths = [os.path.join(self.label_directory, file_name) for file_name in os.listdir(self.label_directory) if
                 file_name.endswith(".txt") and "classes" not in file_name]
        self.setMaximum.emit((len(paths)))
        self.setText.emit(self.hint)
        for index, label_path in enumerate(paths):
            width, height = get_size(os.path.join(self.image_directory, self.search.search(label_path)))
            annos = get_annotation(label_path, self.name_to_image_id, annotation_id, width, height)
            annotation_id += len(annos)
            self.annotations.extend(annos)
            self.setProgress.emit(index + 1)
            self.setDetailedText.emit(f"正在搜索 {label_path} {index + 1}/{len(paths)}")
        self.has_finished.emit()


class YoloSearch:
    def __init__(self, image_path):
        self.image_path = image_path
        self.files = os.listdir(image_path)

    def search(self, label_path):
        for one in self.files:
            if os.path.basename(one).split('.')[0] == os.path.basename(label_path).split('.')[0]:
                return one


def yolo_to_coco(yolo_image_path, yolo_label_path, coco_image_path, coco_label_path, index, yolo_classes_name="classes.txt"):
    coco = {'categories': get_classes(os.path.join(yolo_label_path, yolo_classes_name))}
    get_images = GetImages(yolo_image_path)
    window = ProcessWindow(get_images, title="正在生成图片信息")
    if window.exec_() == window.Rejected:
        return 1
    coco['images'] = get_images.images
    name_to_image_id = get_images.name_to_image_id
    annotation = GetAnnotations(yolo_label_path, yolo_image_path, name_to_image_id)
    window = ProcessWindow(annotation, title='正在生成标签信息')
    if window.exec_() == window.Rejected:
        return 1
    coco['annotations'] = annotation.annotations
    copy = CopyDir(yolo_image_path, coco_image_path, index, "正在拷贝数据集图片")
    window = ProcessWindow(copy, title="正在拷贝数据集图片")
    if window.exec_() == window.Rejected:
        return 1
    change_log = ChangeLog.load(index)
    with open(coco_label_path, 'w') as f:
        json.dump(coco, f, indent=4, ensure_ascii=False)
        change_log.append(coco_label_path)
        change_log.save(index)
    return 0
