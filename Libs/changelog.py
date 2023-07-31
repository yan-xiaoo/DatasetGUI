import os


if not os.path.exists("dataset/changelog"):
    os.makedirs("dataset/changelog")


def delete_changelog(index: int):
    if index is None:
        return
    os.remove(f"dataset/changelog/{index}.txt")


class ChangeLog(list):
    def save(self, index: int):
        with open(f"dataset/changelog/{index}.txt", "w") as f:
            f.write("\n".join(self))

    @classmethod
    def load(cls, index: int):
        try:
            with open(f"dataset/changelog/{index}.txt", "r") as f:
                return cls(f.read().split("\n"))
        except FileNotFoundError:
            return cls()


if __name__ == "__main__":
    os.chdir("..")
    changelog = ChangeLog.load(0)
    changelog.append("1.txt")
    changelog.append("2.txt")
    changelog.save(0)
    changelog = ChangeLog.load(0)
    print(changelog)
