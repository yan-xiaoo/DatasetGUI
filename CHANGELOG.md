# Change log

部分较为重要的新功能和修复会在这里记录。

## [1.0.2] - 2023-10-20

### Added

- 添加了一项对数据集的检查：可以检查数据集中每一种类别的关键点个数是否正确。
- 添加了license, changelog, requirements.txt, readme等说明性文件

## [1.0.1] - 2023-10-6

### Changed

- 去除了依赖 pycocotools 。操作 coco 数据集的功能如今被内建在程序中。

  这是因为 pycocotools 包依赖了太多的其他Python包，而且这些包都用不到。下载它们非常浪费空间。

### Fixed

- 修正了转换coco数据集到yolo时，进度条有时不会变化的问题
- 修正了转换coco数据集到yolo时，changelog文件出现记录错误，导致无法完全删除生成的数据集的问题
- 修复了 Ubuntu 下「在系统中显示」无法正常使用的问题

