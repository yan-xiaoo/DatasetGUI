from .process_window import ProcessFunction
from .changelog import ChangeLog, delete_changelog
import os
import shutil


class CopyDir(ProcessFunction):
    def __init__(self, src, dst, index=None, description="正在拷贝数据集文件"):
        super().__init__()
        self.src = src
        self.dst = dst
        self.index = index if index is not None else "temp"
        self.description = description
        self.change_log = ChangeLog.load(self.index)

    def run(self):
        self.setText.emit(self.description)
        for root, dirs, files in os.walk(self.src):
            maximum = len(files)
            self.setMaximum.emit(maximum)
            i = 0
            for f in files:
                i += 1
                src_file = os.path.join(root, f)
                dst_file = src_file.replace(self.src, self.dst)
                if os.path.exists(dst_file):
                    continue
                self.setDetailedText.emit(f"正在复制 {dst_file} {i}/{maximum}")
                # print("Copying file from", src_file, "to", dst_file)
                self.copyfile(src_file, dst_file)
                self.setProgress.emit(i)

                if not self.can_run:
                    self.setText.emit("正在删除已复制的文件……")
                    self.setMaximum.emit(len(self.change_log))
                    for i in range(len(self.change_log) - 1, -1, -1):
                        self.setProgress.emit(i)
                        f = self.change_log[i]
                        print("Removing ", f)
                        if os.path.isfile(f):
                            os.remove(f)
                        elif os.path.isdir(f):
                            os.rmdir(f)
                        self.setDetailedText.emit(f"正在删除 {os.path.relpath(f, 'dataset')} {i}/{len(self.change_log)}")
                    self.stopped.emit()
                    return
        self.change_log.save(self.index)
        self.has_finished.emit()
        return

    def copyfile(self, src, dst):
        try:
            shutil.copyfile(src, dst)
        except FileNotFoundError:
            self.makedirs(os.path.dirname(dst))
            shutil.copyfile(src, dst)
        self.change_log.append(os.path.abspath(dst))

    def makedirs(self, directory):
        try:
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))
        except FileNotFoundError:
            self.makedirs(os.path.dirname(directory))
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))


class ClearDir(ProcessFunction):
    def __init__(self, index, description="正在清除数据集文件"):
        super().__init__()
        self.index = index
        self.description = description

    def run(self):
        log = ChangeLog.load(self.index)
        self.setMaximum.emit(len(log))
        self.setText.emit(self.description)
        for i in range(len(log) - 1, -1, -1):
            self.setProgress.emit(i)
            f = log[i]
            print("Removing ", f)
            if os.path.isfile(f):
                os.remove(f)
            elif os.path.isdir(f):
                try:
                    os.rmdir(f)
                except OSError:
                    print(f"Failed to remove {f}, it is not empty")
            self.setDetailedText.emit(f"正在删除 {os.path.relpath(f, 'dataset')} {i}/{len(log)}")
        delete_changelog(self.index)
        self.has_finished.emit()
        return


class CopyCertainImage(ProcessFunction):
    def __init__(self, image_dir, image_name, dst_dir, id_, text=None):
        super().__init__()
        self.image_directory = image_dir
        self.image_name = image_name
        self.dst_dir = dst_dir
        self.id_ = id_
        self.text = text
        self.change_log = ChangeLog.load(id_)

    def run(self):
        self.setText.emit(self.text)
        self.setMaximum.emit(len(self.image_name))
        maximum = len(self.image_name)
        for index in range(len(self.image_name)):
            src_file = os.path.join(self.image_directory, self.image_name[index])
            dst_file = os.path.join(self.dst_dir, self.image_name[index])
            self.setDetailedText.emit(f"正在复制 {dst_file} {index}/{maximum}")
            print("Copying file from", src_file, "to", dst_file)
            self.copyfile(src_file, dst_file)
            self.setProgress.emit(index)

            if not self.can_run:
                self.setText.emit("正在删除已复制的文件……")
                self.setMaximum.emit(len(self.change_log))
                for i in range(len(self.change_log) - 1, -1, -1):
                    self.setProgress.emit(i)
                    f = self.change_log[i]
                    print("Removing ", f)
                    if os.path.isfile(f):
                        os.remove(f)
                    elif os.path.isdir(f):
                        os.rmdir(f)
                    self.setDetailedText.emit(f"正在删除 {os.path.relpath(f, 'dataset')} {i}/{len(self.change_log)}")
                self.stopped.emit()
                return
        self.change_log.save(self.id_)
        self.has_finished.emit()

    def copyfile(self, src, dst):
        try:
            shutil.copyfile(src, dst)
        except FileNotFoundError:
            self.makedirs(os.path.dirname(dst))
            shutil.copyfile(src, dst)
        self.change_log.append(os.path.abspath(dst))

    def makedirs(self, directory):
        try:
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))
        except FileNotFoundError:
            self.makedirs(os.path.dirname(directory))
            os.mkdir(directory)
            self.change_log.append(os.path.abspath(directory))