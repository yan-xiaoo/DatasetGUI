from pycocotools import coco
import json


def clean_ip(coco_file: coco.COCO):
    for image in coco_file.imgs.copy().values():
        if len(coco_file.getAnnIds(imgIds=image['id'])) == 0:
            coco_file.dataset['images'].remove(image)
            coco_file.imgs.pop(image['id'])

    for category in coco_file.cats.copy().values():
        if len(coco_file.getImgIds(catIds=category['id'])) == 0:
            coco_file.dataset['categories'].remove(category)
            coco_file.cats.pop(category['id'])
    return coco_file


def clean(coco_path):
    coco_file = coco.COCO(coco_path)
    clean_ip(coco_file)
    with open(coco_path, 'w') as f:
        json.dump(coco_file.dataset, f, indent=4, ensure_ascii=False)


def check_coco(coco_path):
    coco_file = coco.COCO(coco_path)
    result = []
    if "images" not in coco_file.dataset:
        result.append("数据集中不包含图片信息")
    if "annotations" not in coco_file.dataset:
        result.append("数据集中不包含标注信息")
    if "categories" not in coco_file.dataset:
        result.append("数据集中不包含类别信息")
    number = 0
    file_name = None
    for image in coco_file.imgs.copy().values():
        if len(coco_file.getAnnIds(imgIds=image['id'])) == 0:
            if number == 0:
                file_name = image['file_name']
            number += 1
    if number != 0:
        result.append("图片 {} 等 {} 张图片没有标注".format(file_name, number))

    number = 0
    file_name = None
    for category in coco_file.cats.copy().values():
        if len(coco_file.getImgIds(catIds=category['id'])) == 0:
            if number == 0:
                file_name = category['name']
            number += 1
    if number != 0:
        result.append("类别 {} 等 {} 个类别没有标注".format(file_name, number))

    return result
