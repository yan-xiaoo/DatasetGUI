import json
import os.path
from abc import ABC, abstractmethod

if not os.path.isdir("dataset"):
    os.mkdir("dataset")


class DatasetConfig(ABC):
    def __init__(self, name, image_path, label_path):
        self.name = name
        self.image_path = image_path
        self.label_path = label_path

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name}, image_path={self.image_path}, label_path={self.label_path})"

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
        with open(dst, "w") as f:
            json.dump([dataset.save() for dataset in self], f, ensure_ascii=False, indent=4)

    @classmethod
    def load(cls, src: str):
        with open(src, "r") as f:
            return cls([DatasetConfig.load(config) for config in json.load(f)])


def get_available_id():
    i = 0
    while True:
        if not os.path.exists(f"dataset/{i}"):
            return i
        i += 1


def get_id_by_config(config: DatasetConfig):
    if config.image_path.startswith("dataset/"):
        return int(config.image_path.split("/")[1])
    else:
        return None
