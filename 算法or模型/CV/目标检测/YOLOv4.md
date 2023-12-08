# YOLO-V4  
---
##  Bag of freebies
目的：不增加推理消耗的情况下达到更好的准确性。  

|方法|内容|
|-|-|
|数据增强|photometric distortions、geometric distortions|
|光度畸变|调整亮度、对比度、加入色相、饱和度和噪声|
|几何畸变|随机缩放、裁剪、翻转和旋转|  

##### YOLOv4具体实现方案
|架构|方法|具体|
|-|-|-|
|主干网络|数据增强|CutMix、Mosaic|
||正则化|Dropout|
||我还没搞懂|类别标签平滑|
|检测器|损失|CIoU-Loss|
||归一化|CmBN（cross mini-Batch Normalization）|
|||SAT自对抗训练|
|||敏感性消除|
|||单GT多锚点|
|||余弦退火|
|||最优超参数|
|||随机训练尺寸|

## Bag of specials
目的：增加少量推理消耗，极大提高训练准确性。


##### YOLOv4具体实现方案
|架构|方法|具体|
|-|-|-|
|主干网络|数据增强|CutMix、Mosaic|
||正则化|Dropout|
||我还没搞懂|类别标签平滑|
|检测器|损失|CIoU-Loss|
||归一化|CmBN（cross mini-Batch Normalization）|
|||SAT自对抗训练|
|||敏感性消除|
|||单GT多锚点|
|||余弦退火|
|||最优超参数|
|||随机训练尺寸|