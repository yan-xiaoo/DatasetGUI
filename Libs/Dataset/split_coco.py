from .coco_utils import COCO
import random


def copy_basic_info(src, dst):
    if src.dataset.get('info', 0) != 0:
        dst.dataset["info"] = src.dataset["info"]
    if src.dataset.get('categories', 0) != 0:
        dst.dataset["categories"] = src.dataset["categories"]
    dst.createIndex()


def category_split(annotation_file: str, rate_of_train: float, rate_of_val: float):
    annotation = COCO(annotation_file)
    train_file = COCO()
    val_file = COCO()

    copy_basic_info(annotation, train_file)
    copy_basic_info(annotation, val_file)

    for category_id in annotation.getCatIds():
        category_images = annotation.getImgIds(catIds=category_id)
        num_of_train = int(len(category_images) * rate_of_train)
        num_of_val = int(len(category_images) * rate_of_val)

        # 为了防止没有验证集，将训练集的数量减少
        if num_of_val == 0 and num_of_train > 1 and rate_of_val != 0:
            num_of_val = 1
            num_of_train -= 1

        for _ in range(num_of_train):
            image_id = random.choice(category_images)
            category_images.remove(image_id)
            img = annotation.loadImgs(image_id)[0]
            train_file.imgs[image_id] = img
            anns = annotation.loadAnns(annotation.getAnnIds(imgIds=image_id))[0]
            train_file.anns[image_id] = anns

        for _ in range(num_of_val):
            image_id = random.choice(category_images)
            category_images.remove(image_id)
            img = annotation.loadImgs(image_id)[0]
            val_file.imgs[image_id] = img
            anns = annotation.loadAnns(annotation.getAnnIds(imgIds=image_id))[0]
            val_file.anns[image_id] = anns

    train_file.dataset["images"] = list(train_file.imgs.values())
    train_file.dataset["annotations"] = list(train_file.anns.values())

    val_file.dataset["images"] = list(val_file.imgs.values())
    val_file.dataset["annotations"] = list(val_file.anns.values())

    return train_file, val_file
