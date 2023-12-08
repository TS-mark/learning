# 多目标跟踪MOT（Multiple Object Tracking）
  多目标跟踪，一般简称为MOT(Multiple Object Tracking)，也有一些文献称作MTT(Multiple Target Tracking)。在事先不知道目标数量的情况下，对视频中的行人、汽车、动物等多个目标进行检测并赋予ID进行轨迹跟踪。不同的目标拥有不同的ID，以便实现后续的轨迹预测、精准查找等工作。

  MOT是计算机视觉领域的一项关键技术，在自动驾驶、智能监控、行为识别等方向应用广泛。如下图所示，对于输入视频，输出目标的跟踪结果，包括目标包围框和对应的ID编号。理论上，同一个目标的ID编号保持不变。  
  多目标跟踪中即要面对在单目标跟踪中存在的遮挡、变形、运动模糊、拥挤场景、快速运动、光照变化、尺度变化等挑战，还要面对如轨迹的初始化与终止、相似目标间的相互干扰等复杂问题。因此，多目标跟踪当前仍然是图像处理中的一个极具挑战性的方向，吸引了不少研究人员的长期投入。
  在多目标跟踪领域，常用的跟踪策略是TBD（Tracking-by-Detection，主流）和DFT(Detection-Free Tracking)。TBD，也可叫DBT（Detection-Based-Tracking）。即在每一帧进行目标检测，再利用目标检测的结果来进行目标跟踪，这一步我们一般称之为数据关联（Data Assoiation）。  
  MOT 获取单个连续视频并以特定帧速率 (fps) 将其拆分为离散帧以输出。

### 难点
目标跟踪是一个早已存在的方向，但之前的研究主要集中于单目标跟踪，直到近几年，多目标跟踪才得到研究者的密切关注。与其它计算机视觉任务相比，多目标跟踪任务主要存在以下研究难点：

准确的对象检测的问题是未能检测到对象或者为检测到的对象分配错误的类别标签或错误地定位已识别的对象：

* ID Switching发生在两个相似的物体重叠或混合时，导致身份切换；因此，很难跟踪对象 ID。

* 背景失真：复杂的背景使得在物体检测过程中难以检测到小物体

* 遮挡：对象被另一个对象隐藏或遮挡时会产生这个问题。

* 多个空间空间、变形或对象旋转

* 由于运动模糊而在相机上捕获的视觉条纹或拖尾

好的MOT算法特点：
* 通过在每帧的精确位置识别正确数量的跟踪器来跟踪对象。

* 通过长期一致地跟踪单个对象来识别对象，

* 尽管有遮挡、照明变化、背景、运动模糊等，仍可跟踪对象。

* 快速检测和跟踪物体


MOT方法：
1. tracking by detection 检测器和匹配机制 --sort、deepsort、strongsort
2. joint detection and tracking -一个模型可以同时完成检测和匹配 --JDE、FairMOT、CenterTrack、QDTrack
3. Tracking by Attention -- TrackFormer、GTR


# 多目标跟踪分割（Multi-Object Tracking and Segmentation - MOTS）
  和MOT的区别：MOT输出的是bounding box，MOTS输出的是mask