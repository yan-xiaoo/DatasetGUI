from pycocotools.coco import COCO
import os
from ..changelog import ChangeLog
from ..process_window import ProcessFunction

images_nums = 0
category_nums = 0
bbox_nums = 0


# 将类别名字和id建立索引
def catid2name(coco):
    classes = dict()
    for cat in coco.dataset['categories']:
        classes[cat['id']] = cat['name']
    return classes


# 将[xmin,ymin,xmax,ymax]转换为yolo格式[x_center, y_center, w, h](做归一化)
def xyxy2xywhn(object_, width, height):
    cat_id = object_[0]
    xn = object_[1] / width
    yn = object_[2] / height
    wn = object_[3] / width
    hn = object_[4] / height
    for index in range(5, len(object_)):
        object_[index][0] = object_[index][0] / width
        object_[index][1] = object_[index][1] / height
    out = "{} {} {} {} {}".format(cat_id, xn, yn, wn, hn)
    for index in range(5, len(object_)):
        out += " {} {}".format(object_[index][0], object_[index][1])
    return out


def save_anno_to_txt(images_info, save_path):
    filename = images_info['filename']
    txt_name = filename[:-3] + "txt"
    with open(os.path.join(save_path, txt_name), "w") as f:
        for obj in images_info['objects']:
            line = xyxy2xywhn(obj, images_info['width'], images_info['height'])
            f.write("{}\n".format(line))


# 利用cocoAPI从json中加载信息
class LoadCoco(ProcessFunction):
    def __init__(self, anno_file, xml_save_path, id_, hint="正在生成coco数据集"):
        super().__init__()
        self.anno_file = anno_file
        self.xml_save_path = xml_save_path
        self.id_ = id_
        self.hint = hint
        self.change_log = ChangeLog.load(id_)

    def run(self):
        coco = COCO(self.anno_file)
        classes = catid2name(coco)
        imgIds = coco.getImgIds()
        classesIds = coco.getCatIds()
        self.setText.emit(self.hint)
        if not os.path.isdir(self.xml_save_path):
            self.makedirs(self.xml_save_path)

        with open(os.path.join(self.xml_save_path, "classes.txt"), 'w') as f:
            for id_ in classesIds:
                f.write("{}\n".format(classes[id_]))
                self.change_log.append(os.path.join(self.xml_save_path, "classes.txt"))

        self.setMaximum.emit(len(imgIds))
        for index, imgId in enumerate(imgIds):
            info = {}
            img = coco.loadImgs(imgId)[0]
            filename = img['file_name']
            width = img['width']
            height = img['height']
            info['filename'] = filename
            info['width'] = width
            info['height'] = height
            annIds = coco.getAnnIds(imgIds=img['id'], iscrowd=None)
            anns = coco.loadAnns(annIds)

            categories = coco.dataset['categories']
            min_category = 100000
            for cate in categories:
                if cate['id'] < min_category:
                    min_category = cate['id']

            objs = []
            for ann in anns:
                # bbox:[x,y,w,h]

                bbox = list(map(float, ann['bbox']))
                xc = bbox[0] + bbox[2] / 2.
                yc = bbox[1] + bbox[3] / 2.
                w = bbox[2]
                h = bbox[3]

                segmentation = []
                for index in range(0, len(ann['segmentation'][0]), 2):
                    segmentation.append(
                        [float(ann['segmentation'][0][index]), float(ann['segmentation'][0][index + 1])])

                obj = [ann['category_id'] - min_category, xc, yc, w, h]
                obj.extend(segmentation)
                objs.append(obj)
            info['objects'] = objs
            if len(objs) > 0:
                save_anno_to_txt(info, self.xml_save_path)
                self.change_log.append(os.path.join(self.xml_save_path, info['filename'][:-3] + "txt"))

            self.setProgress.emit(index + 1)
            self.setDetailedText.emit(f"正在生成 {os.path.join(self.xml_save_path, info['filename'][:-3] + 'txt')} {index + 1}/{len(imgIds)}")
        self.change_log.save(id_)
        self.has_finished.emit()

    def makedirs(self, directory):
        try:
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))
        except FileNotFoundError:
            self.makedirs(os.path.dirname(directory))
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))
