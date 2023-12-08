# pytorch自动混合精度(AMP)训练

摘自[Pytorch自动混合精度(AMP)训练](https://blog.csdn.net/ytusdc/article/details/122152244)  



pytorch的`torch.cuda.amp`采用自动混合精度训练，不需要加载NVIDIA的apex库。

## 什么是AMP

默认情况下，大多数深度学习框架都采用32位浮点算法进行训练。2017年，NVIDIA研究了一种用于混合精度训练的方法，该方法在训练网络时将单精度（FP32）与半精度(FP16)结合在一起，并使用相同的超参数实现了与FP32几乎相同的精度。

## 优势和劣势
优势：
1. 减少显存使用
2. 加速训练和推理的计算
劣势：
1. 溢出错误：由于FP16的动态范围比FP32的狭窄很多，在计算过程中很容易出现上溢出和下溢出，溢出后计算值就会出现"NaN"问题。在深度学习中，由于激活函数的梯度比权重梯度小，更容易出现下溢出的情况。
2. 舍入误差：当梯度过小时，小于当前区间内的最小间隔时，该次梯度更新可能会失败。
浮点数越小，引起的舍入误差就越大，对足够小的浮点数执行任何操作都会让该值变为零，这就是underflowing。
![](./img/amp.png)


注意，浮点数越小，引起的舍入误差就越大。 对“足够小“的浮点数执行的任何操作都会将该值四舍五入到零！ 这就是所谓的underflowing，这是一个问题，因为在反向传播中很多甚至大多数梯度更新值都非常小，但不为零。 在反向传播中舍入误差累积可以把这些数字变成0或者 nans; 这会导致不准确的梯度更新或者梯度更新可能会失败，影响你的网络收敛。

## 解决问题的办法
1. 混合精度训练
  在某些模型中，fp16矩阵乘法的过程中，需要利用 fp32 来进行矩阵乘法中间的累加(accumulated)，然后再将 fp32 的值转化为 fp16 进行存储。 换句不太严谨的话来说，也就是在内存中用FP16做储存和乘法从而加速计算，而用FP32做累加避免舍入误差。混合精度训练的策略有效地缓解了舍入误差的问题。

在torch的amp中，以下操作会转换为半精度浮点torch.halftensor
```
__matmul__
addbmm
addmm
addmv
addr
baddbmm
bmm
chain_matmul
conv1d
conv2d
conv3d
conv_transpose1d
conv_transpose2d
conv_transpose3d
linear
matmul
mm
mv
prelu
```

2. 动态损失放大

  Pytorch可以通过使用torch.cuda.amp.GradScaler，通过放大loss的值来防止梯度的underflow（只在BP时传递梯度信息使用，真正更新权重时还是要把放大的梯度再unscale回去）

损失放大的思路是：
    1. 反向传播前，将损失变化手动增大2^k倍，因此反向传播时得到的中间变量（激活函数梯度）则不会溢出；
    2. 反向传播后，将权重梯度缩小2^k倍，恢复正常值。

## 如何在pytorch中使用自动混合精度？

```python
from torch.cuda.amp import autocast, GradScaler
 
# 创建model，默认是torch.FloatTensor
model = Net().cuda()
optimizer = optim.SGD(model.parameters(), ...)
 
# 在训练最开始之前实例化一个GradScaler对象
scaler = GradScaler()
 
for epoch in epochs:
    for input, target in data:
        optimizer.zero_grad()
 
        # 前向过程(model + loss)开启 autocast
        with autocast():
            output = model(input)
            loss = loss_fn(output, target)
 
        # Scales loss. 为了梯度放大.
        scaler.scale(loss).backward()
 
        # scaler.step() 首先把梯度的值unscale回来.
        # 如果梯度的值不是 infs 或者 NaNs, 那么调用optimizer.step()来更新权重,
        # 否则，忽略step调用，从而保证权重不更新（不被破坏）
        scaler.step(optimizer)
 
        # 准备着，查看是否要增大scaler
        scaler.update()
```

## 流程

总结amp的流程是：
1. 维护一个 FP32 数值精度模型的副本
2. 在每个iteration
    1. 拷贝并且转换成 FP16 模型
    2. 前向传播（FP16 的模型参数）
    3. loss 乘 scale factor s
    4. 反向传播（FP16 的模型参数和参数梯度）
    5. 参数梯度乘 1/s
    6. 利用 FP16 的梯度更新 FP32 的模型参数


autocast自动转换流程，核心就是`with autocast():`中，对于部分算子支持相关计算。
```python
import torch
from torch.cuda.amp import autocast
# Creates some tensors in default dtype (here assumed to be float32)
a_float32 = torch.rand((8, 8), device="cuda")
b_float32 = torch.rand((8, 8), device="cuda")
c_float32 = torch.rand((8, 8), device="cuda")
d_float32 = torch.rand((8, 8), device="cuda")

with autocast():
    # torch.mm is on autocast's list of ops that should run in float16.
    e_float16 = torch.mm(a_float32, b_float32)
    # Also handles mixed input types
    f_float16 = torch.mm(d_float32, e_float16)

# After exiting autocast, calls f_float16.float() to use with d_float32
g_float32 = torch.mm(d_float32, f_float16.float())
```