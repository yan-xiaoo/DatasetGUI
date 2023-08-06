import json
import os.path
import sys
from abc import ABC, abstractmethod
import enum

if not os.path.isdir("dataset"):
    os.mkdir("dataset")


class DataType(enum.Enum):
    SINGLE = 0
    TRAIN = 1
    VAL = 2
    MERGED = 3


class MergedDatasetConfig(ABC):
    """
    表示一个训练集和一个验证集组合成的数据集
    仅仅可以用来表示标准yolo和coco数据集。
    标准的yolo数据集
    dataset
    - images
    - - train
    - - val
    - labels
    - - train
    - - val
    标准的coco数据集：
    dataset
    - images
    - - train
    - - val
    - train.json
    - val.json
    """
    def __init__(self, train_dataset, val_dataset, common_image_path=None, common_label_path=None):
        """
        创建一个组合数据集
        :param train_dataset: 训练集对象
        :param val_dataset: 验证集对象
        :param common_image_path: 训练集与验证集共同的图片路径。这个路径需要满足：包含训练集与验证集所有的图片数据
        :param common_label_path: 训练集与验证集共同的标签路径
        """
        assert os.path.dirname(train_dataset.image_path) == os.path.dirname(val_dataset.image_path), "两数据集图片文件夹不再同一文件夹下"
        assert train_dataset.type_ == val_dataset.type_, "不是相同类型的数据集"
        assert os.path.dirname(train_dataset.label_path) == os.path.dirname(val_dataset.label_path), "两数据集标签文件夹不在同一文件夹下"
        self.train = train_dataset
        self.val = val_dataset
        if common_image_path is None:
            self.image_path = os.path.dirname(train_dataset.image_path)
        else:
            self.image_path = common_image_path
        if common_label_path is None:
            self.label_path = os.path.dirname(train_dataset.label_path)
        else:
            self.label_path = common_label_path

        self.train.parent = self
        self.train.data_type = DataType.TRAIN
        self.val.parent = self
        self.val.data_type = DataType.VAL

    def __getitem__(self, item):
        if item == 0:
            return self.train
        elif item == 1:
            return self.val
        else:
            raise IndexError("Index out of range: 0, 1")

    def __setitem__(self, key, value):
        if key == 0:
            self.train = value
        elif key == 1:
            self.val = value
        else:
            raise IndexError("Index out of range: 0, 1")

    def __repr__(self):
        return f"{self.__class__.__name__}(train={self.train}, val={self.val}, common_image_path={self.image_path}, common_label_path={self.label_path})"

    @property
    def type_(self):
        return self.train.type_

    def save(self):
        return {"train": self.train.save(), "val": self.val.save(), "common_image_path": self.image_path, "common_label_path": self.label_path, "type": self.type_}

    @classmethod
    def load(cls, config):
        return cls(train_dataset=DatasetConfig.load(config["train"]), val_dataset=DatasetConfig.load(config["val"]), common_image_path=config["common_image_path"], common_label_path=config["common_label_path"])

    def is_merged(self):
        return True

    data_type = DataType.MERGED


class DatasetConfig(ABC):
    def __init__(self, name, image_path, label_path):
        self.name = name
        self.image_path = image_path
        self.label_path = label_path
        self.parent = None

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, image_path={self.image_path}, label_path={self.label_path}, data_type={self.data_type})"

    @property
    @abstractmethod
    def type_(self):
        pass

    def save(self):
        return {"name": self.name, "image_path": self.image_path, "label_path": self.label_path, "type": self.type_}

    @classmethod
    def load(cls, config):
        return cls.from_type(config["type"], config)

    @classmethod
    def from_type(cls, type_, config):
        if type_ == "coco":
            return CocoDataset(name=config["name"], image_path=config["image_path"], label_path=config["label_path"])
        elif type_ == 'yolo':
            return YoloDataset(name=config["name"], image_path=config["image_path"], label_path=config["label_path"])
        else:
            return cls(name=config["name"], image_path=config["image_path"], label_path=config["label_path"])

    def is_merged(self):
        return False

    data_type = DataType.SINGLE


class CocoDataset(DatasetConfig):
    @property
    def type_(self):
        return "coco"


class YoloDataset(DatasetConfig):
    @property
    def type_(self):
        return 'yolo'


class DatasetManager(list):
    def save(self, dst: str):
        with open(dst, 'w') as f:
            result = []
            parents = []
            for config in self:
                if config.data_type in [DataType.TRAIN, DataType.VAL]:
                    if config.parent not in parents:
                        parents.append(config.parent)
                        result.append(config.parent.save())
                else:
                    result.append(config.save())
            json.dump(result, f, indent=4, ensure_ascii=False)

    @classmethod
    def load(cls, src: str):
        result = []
        with open(src, "r") as f:
            configs = json.load(f)
            for config in configs:
                if "train" in config:
                    parent = MergedDatasetConfig.load(config)
                    result.append(parent.train)
                    result.append(parent.val)
                else:
                    result.append(DatasetConfig.load(config))
        return cls(result)


def get_available_id():
    i = 0
    while True:
        if not os.path.exists(f"dataset/{i}"):
            return i
        i += 1


def get_id_by_config(config: DatasetConfig):
    if (config.image_path.startswith("dataset/") or os.path.relpath(config.image_path).startswith("dataset/")) \
            and (config.label_path.startswith("dataset/") or os.path.relpath(config.label_path).startswith("dataset/")):
        if 'win32' in sys.platform:
            spliter = '\\'
        else:
            spliter = '/'
        try:
            if int(os.path.relpath(config.image_path).split(spliter)[1]) == int(os.path.relpath(config.label_path).split(spliter)[1]):
                return int(os.path.relpath(config.image_path).split(spliter)[1])
            elif int(config.image_path.split(spliter)[1]) == int(config.label_path.split(spliter)[1]):
                return int(config.image_path.split(spliter)[1])
            else:
                return None
        except ValueError:
            return None


if __name__ == "__main__":
    os.chdir("..")
    m = DatasetManager()
    train = YoloDataset(name="train", image_path="dataset/0/images/train", label_path="dataset/0/labels/train")
    val = YoloDataset(name="val", image_path="dataset/0/images/val", label_path="dataset/0/labels/val")
    MergedDatasetConfig(train, val)
    m.append(train)
    m.append(val)
    m.append(CocoDataset(name="test", image_path="dataset/1/images", label_path="dataset/1/dataset.json"))
    print(m)
    m.save("temp.json")

    m2 = DatasetManager.load("temp.json")
    print(m2)
    print(m2[0].parent)
