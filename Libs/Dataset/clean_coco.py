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
