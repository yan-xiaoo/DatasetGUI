from pycocotools import coco
import json
import os


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


def check_coco_detailed(coco_path):
    coco_file = coco.COCO(coco_path)
    result = []
    if "images" not in coco_file.dataset:
        result.append("数据集中不包含图片信息")
    if "annotations" not in coco_file.dataset:
        result.append("数据集中不包含标注信息")
    if "categories" not in coco_file.dataset:
        result.append("数据集中不包含类别信息")
    for image in coco_file.imgs.copy().values():
        if len(coco_file.getAnnIds(imgIds=image['id'])) == 0:
            result.append("图片 {} 没有标注".format(image['file_name']))

    for category in coco_file.cats.copy().values():
        if len(coco_file.getImgIds(catIds=category['id'])) == 0:
            result.append("类别 {} 没有标注".format(category['name']))

    return result


def check_coco_images(coco_image_path, coco_label_path):
    coco_file = coco.COCO(coco_label_path)
    result = []
    for image in coco_file.dataset['images']:
        if not os.path.exists(os.path.join(coco_image_path, image['file_name'])):
            result.append("标注过的图片 {} 不存在".format(image['file_name']))
    return result
