# torchvision

---
## torchvision由四个模块组成
1. [<font color = "red">torchvision.datasets</font> : Data loaders for popular vision datasets](#datasets)
2. [<font color = "red">torchvision.models</font> : Definitions for popular model architectures, such as AlexNet, VGG, and ResNet and pre-trained models.](#models) 
3. [<font color = "red">torchvision.transforms</font> : Common image transformations such as random crop, rotations etc.](#transforms)
4. [<font color = "red">torchvision.utils</font> : Useful stuff such as saving tensor (3 x H x W) as image to disk, given a mini-batch creating a grid of images, etc.](#utils)

---
### <a id="datasets">torchvision.datasets</a>
torchvision.datasets继承于torch.utils.data.Dataset，可以使用torch.utils.data.DataLoader对其进行处理。（多线程）  
不过我感觉还是torch.utils.data.Dataset好用
```python
torch.utils.data.DataLoader(coco_cap, batch_size=args.batchSize, shuffle=True, num_workers=args.nThreads)

```

---
### <a id="models">torchvision.models</a>
models定义了几个模型：
1. AlexNet
2. VGG ：models.vgg11(); models.vgg13(); models.vgg16(); models.vgg19()
3. ResNet: models.resnet18(); models.resnet34(); models.resnet50(); models.resnet101(); models.resnet152()
4. squeezenet: models.squeezenet1_0()
5. mobilenet: mobilenet_v2(); mobilenet_v3_large(); mobilenet_v3_small()  

调用方法：
```python
import torchvision.models as models

resnet18 = models.resnet18(pretrained=True)
alexnet = models.alexnet(pretrained=True)
vgg16 = models.vgg16(pretrained=True)
squeezenet = models.squeezenet1_0(pretrained=True)
densenet = models.densenet161(pretrained=True)
inception = models.inception_v3(pretrained=True)
googlenet = models.googlenet(pretrained=True)
shufflenet = models.shufflenet_v2_x1_0(pretrained=True)
mobilenet_v2 = models.mobilenet_v2(pretrained=True)
mobilenet_v3_large = models.mobilenet_v3_large(pretrained=True)
mobilenet_v3_small = models.mobilenet_v3_small(pretrained=True)
resnext50_32x4d = models.resnext50_32x4d(pretrained=True)
wide_resnet50_2 = models.wide_resnet50_2(pretrained=True)
mnasnet = models.mnasnet1_0(pretrained=True)
efficientnet_b0 = models.efficientnet_b0(pretrained=True)
efficientnet_b1 = models.efficientnet_b1(pretrained=True)
efficientnet_b2 = models.efficientnet_b2(pretrained=True)
efficientnet_b3 = models.efficientnet_b3(pretrained=True)
efficientnet_b4 = models.efficientnet_b4(pretrained=True)
efficientnet_b5 = models.efficientnet_b5(pretrained=True)
efficientnet_b6 = models.efficientnet_b6(pretrained=True)
efficientnet_b7 = models.efficientnet_b7(pretrained=True)
regnet_y_400mf = models.regnet_y_400mf(pretrained=True)
regnet_y_800mf = models.regnet_y_800mf(pretrained=True)
regnet_y_1_6gf = models.regnet_y_1_6gf(pretrained=True)
regnet_y_3_2gf = models.regnet_y_3_2gf(pretrained=True)
regnet_y_8gf = models.regnet_y_8gf(pretrained=True)
regnet_y_16gf = models.regnet_y_16gf(pretrained=True)
regnet_y_32gf = models.regnet_y_32gf(pretrained=True)
regnet_x_400mf = models.regnet_x_400mf(pretrained=True)
regnet_x_800mf = models.regnet_x_800mf(pretrained=True)
regnet_x_1_6gf = models.regnet_x_1_6gf(pretrained=True)
regnet_x_3_2gf = models.regnet_x_3_2gf(pretrained=True)
regnet_x_8gf = models.regnet_x_8gf(pretrained=True)
regnet_x_16gf = models.regnet_x_16gf(pretrained=True)
regnet_x_32gf = models.regnet_x_32gf(pretrained=True)
```
---
### <a id="transforms">torchvision.transforms</a>
(transforming and augment images)图像增强、转换  
torchvision.transforms包含常见的图像变化（预处理），通过可以使用compose进行组合链接，torchvision.transforms.Compose。  
大部分transformations支持PIL和tensor图像
torchvision.transforms可以分为以下几类：
```python
# transforms的常见用法：
transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
])
#### 图像转换、增强
|函数|含义|
|-|-|
|CenterCrop(size)|在中心裁剪给定图像|
|ColorJitter([brightness,contrast,...])|随机改变亮度(brightness)、对比度(contrast)、饱和度(saturation)和色调(hue)|
|FiveCrop(size)|对给定图像进行四个角裁剪和中央裁剪|
|TenCrop(size)|在FiveCrop基础上加了翻转 版本|
|Grayscale([num_output_channels])|图像灰度变换|
|Pad(padding[,fill,padding_mode])|使用给定"pad"值再所有边上填充给定图像|
|RandomAffine(drees[,translate,scale,...])|保持图像中心不变的随机仿射变换|
|RandomApply(transforms[,p])|以概率p采用一系列的transforms|
|RandomCrop(size[,padding,pad_if_needed,...])|裁剪图像的随机区域|
|RandomGrayscale[p]|随机对图像进行灰度变换|
|RandomHorizontalFlip([p])|概率水平翻转图像|
|resize(size[, interpolation, max_size])|resize|
|GaussianBlur(kernel_size[,sigma])|给图片增加高速模糊|

#### 转换类型
|函数|含义|
|-|-|
|ToPILImage([mode])||
|ToTensor()|将PIL转换为Tensor|
|PILToTensor()|转换为对应数值的Tensor|
注：这里使用ToTensor时，将图像取值为[0,255]的像素缩放成[0.0,1.0],如果使用PILToTensor，则不会进行这个缩放

---
#### *一. Transforms on PIL.Image*
1. Scale(size, interpolation=Image.BILINEAR)
2. CenterCrop(size) - center-crops the image to the given size
3. RandomCrop(size, padding=0)
4. RandomHorizontalFlip()
5. RandomSizedCrop(size, interpolation=Image.BILINEAR)
6. Pad(padding, fill=0)

#### *二. Transforms on torch.Tensor*
1. Normalize(mean, std)
作用: Given mean: (R, G, B) and std: (R, G, B), will normalize each channel of the torch.*Tensor, i.e. channel = (channel - mean) / std

#### *三. Conversion Transforms 数据格式转换操作*
1. ToTensor()
作用: Converts a PIL.Image (RGB) or numpy.ndarray (H x W x C) in the range [0, 255] to a torch.FloatTensor of shape (C x H x W) in the range [0.0, 1.0]

#### *四. Generic Transforms 一般的变化操作*
1. Lambda(lambda) # 自己定义一个python lambda表达式, applies it to the input img and returns it.
举例: transforms.Lambda(lambda x: x.add(10))　 # 将每个像素值加10

---
### <a id="utils">torchvision.utils</a>
目前就两个功能
1. torchvision.utils.make_grid(tensor, nrow = 8, padding = 2, normalize = False, range = None, scale_each = False)  

作用: 输入4D mini-batch Tensor of shape (B x C x H x W)或者a list of images all of the same size, 然后用这些图片生成一个大的图片.(图片中每格子为单张图片)  
normalize=True will shift the image to the range (0, 1), by subtracting the minimum and dividing by the maximum pixel value.
if range=(min, max) where min and max are numbers, then these numbers are used to normalize the image.  
scale_each=True will scale each image in the batch of images separately rather than computing the (min, max) over all images.  


---
## 参考
[torchvision官网](https://pytorch.org/vision/stable/index.html)