from filetype import is_image
import os
from .yolo_to_coco import YoloSearch
from ..process_window import ProcessFunction


def check_yolo_dataset(yolo_image_directory, yolo_label_directory):
    result = []
    searcher = YoloSearch(yolo_label_directory)
    for file in os.listdir(yolo_image_directory):
        if is_image(os.path.join(yolo_image_directory, file)):
            if not os.path.isfile(os.path.join(yolo_label_directory, searcher.search(file))):
                print(os.path.join(yolo_label_directory, searcher.search(file)))
                result.append("图片 {} 没有标注".format(file))

    try:
        with open(os.path.join(yolo_label_directory, "classes.txt")) as f:
            classes_name = [one.strip() for one in f.readlines()]
            classes = list(range(len(classes_name)))
            id_to_class_name = {i: name for i, name in enumerate(classes_name)}
    except FileNotFoundError:
        result.append("数据集中未找到分类描述文件 classes.txt")
        return result

    for label in os.listdir(yolo_label_directory):
        try:
            with open(os.path.join(yolo_label_directory, label)) as f:
                class_ = [int(one.split(' ')[0]) for one in f.readlines()]
        except (FileNotFoundError, UnicodeDecodeError, ValueError):
            pass
        else:
            for one_class in class_:
                try:
                    classes.remove(one_class)
                except ValueError:
                    pass
        if not classes:
            return result

    for one_class in classes:
        result.append("数据集中未找到分类 {}".format(id_to_class_name[one_class]))
    return result


class CheckYoloDataset(ProcessFunction):
    def __init__(self, yolo_image_dir, yolo_label_dir, hint="正在检查数据集"):
        super().__init__()
        self.yolo_image_directory = yolo_image_dir
        self.yolo_label_directory = yolo_label_dir
        self.hint = hint
        self.result = []

    def run(self):
        searcher = YoloSearch(self.yolo_label_directory)
        self.setText.emit(self.hint)
        files = os.listdir(self.yolo_image_directory)
        len_of_files = len(files)
        self.setMaximum.emit(len_of_files)
        for index, file in enumerate(files):
            if is_image(os.path.join(self.yolo_image_directory, file)):
                label_name = searcher.search(file)
                if label_name is not None:
                    if not os.path.isfile(os.path.join(self.yolo_label_directory, label_name)):
                        self.result.append("图片 {} 没有标注".format(file))
                else:
                    self.result.append("图片 {} 没有标注".format(file))
            self.setProgress.emit(index + 1)
            self.setDetailedText.emit("正在检查图片 {} {}/{}".format(file, index + 1, len_of_files))

        try:
            with open(os.path.join(self.yolo_label_directory, "classes.txt")) as f:
                classes_name = [one.strip() for one in f.readlines()]
                classes = list(range(len(classes_name)))
                id_to_class_name = {i: name for i, name in enumerate(classes_name)}
        except FileNotFoundError:
            self.result.append("数据集中未找到分类描述文件 classes.txt")
            self.has_finished.emit()
            return

        files = os.listdir(self.yolo_label_directory)
        len_of_files = len(files)
        self.setMaximum.emit(0)
        for index, label in enumerate(files):
            try:
                with open(os.path.join(self.yolo_label_directory, label)) as f:
                    class_ = [int(float(one.split(' ')[0])) for one in f.readlines()]
            except (FileNotFoundError, UnicodeDecodeError, ValueError):
                pass
            else:
                for one_class in class_:
                    try:
                        classes.remove(one_class)
                    except ValueError:
                        pass
            if not classes:
                self.has_finished.emit()
                return
            self.setDetailedText.emit("正在检查标注文件 {} {}/{}".format(label, index + 1, len_of_files))

        for one_class in classes:
            self.result.append("未找到 classes.txt 中的分类 {}".format(id_to_class_name[one_class]))
        self.has_finished.emit()


def check_yolo_images(yolo_image_path, yolo_label_path):
    result = []
    searcher = YoloSearch(yolo_image_path)
    for file in os.listdir(yolo_label_path):
        if searcher.search(file) is None and file != "classes.txt":
            result.append("标注文件 {} 没有对应的图片".format(file))
    return result
