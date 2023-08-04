import os
import random


def basic_split(label_directory, rate_train, rate_val):
    labels = [one for one in os.listdir(label_directory)]
    train_number = int(rate_train * len(labels))
    val_number = int(rate_val * len(labels))
    if val_number == 0:
        val_number = 1
        train_number -= 1
    if train_number == 0:
        train_number = 1
        val_number -= 1
    train_labels = []
    val_labels = []
    for _ in range(train_number):
        label = random.choice(labels)
        labels.remove(label)
        if label == 'classes.txt':
            continue
        train_labels.append(label)
    for _ in range(val_number):
        label = random.choice(labels)
        labels.remove(label)
        if label == 'classes.txt':
            continue
        val_labels.append(label)
    if labels:
        train_labels.extend(labels)
    return train_labels, val_labels


if __name__ == '__main__':
    train, val = basic_split('../../dataset/3/labels', 0.8, 0.2)
    print(train)
    print(val)
