# shuffle net
---



## shuffle net基础
### 分组卷积
分组卷积是shuffle net的核心，详细请看[分组卷积](./1.分组卷积.md)

### 分组卷积矛盾
group convolution层另一个问题是不同组之间的特征图需要通信，否则就好像分了几个互不相干的路，大家各走各的，会降低网络的特征提取能力，这也可以解释为什么Xception，MobileNet等网络采用密集的1x1 pointwise convolution，因为要保证group convolution之后不同组的特征图之间的信息交流。

## shufflenetV1
* 论文：《ShuffleNet: An Extremely Efficient Convolutional Neural Network for Mobile Devices》
* ShuffleNet是Face++（旷视）在2017年发布的一个高效率可以运行在手机等移动设备的网络结构，论文发表在CVRP2018上。这个新的轻量级网络使用了两个新的操作：
    * pointwise group convolution
    * channel shuffle  


* 核心：
    * 为了达到特征通信的目的，提出了channel shuffle
    * 使用pointwise group convolution来降低1 x 1 卷积的计算复杂度。
### channel shuffle
为了解决分组卷积特征不通信的问题，采用channel shuffle
![](./img/shufflenet.png)


### pointwise group convolution
![](./img/shufflenet2.png)


在保持精度的同时大大降低计算成本。


   （1）使用分组逐点卷积(pointwise group convolution，GConv)来降低1×1卷积的计算复杂度，这个分组逐点卷积跟逐点卷积不一样，是在其基础上分组的。

   （2）使用通道重排操作来帮助信息在特征通道间流动。