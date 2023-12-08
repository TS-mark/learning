# Batch Normalization
---
### BN层主要解决的问题是：
internal covariate shift (内部协变量转移)
内部协变量偏移是指网络在训练过程中，由于网络参数的变化导致网络激活的分布发生变化。这种变化会导致网络训练变慢，梯度消失等问题，限制了深度神经网络的性能和训练速度。


<!-- 由于参数更新，每层输入的特征分布，不再是独立同分布（训练过程中神经网络都在抖动） -->

#### internal covariate shift 会造成的问题：
1. 使模型中的输入输出不符合独立同分布假设，影响模型准确性
    独立同分布假设:      假设训练数据和测试数据是满足相同分布的
2. 下层输入的变化可能趋向于变大或变小，可能导致上层输入落入激活函数的饱和区（这个的解释可参考sigmoid函数，饱和区就是过大或者过小的那一部分），导致梯度消失
3. 上层网络需要适应新的输入数据分布，降低学习速度


batch normalization算法：
$\mu_\beta \leftarrow \frac{1}{m} \sum_{i=1}^m x_i  $
$\sigma^2 \leftarrow \frac{1}{m} \sum_{i=1}^m (x_i - \mu_\beta)^2 $
$\hat{x_i} \leftarrow \frac{x_i-\mu_\beta}{\sqrt{\sigma^2_\beta + \epsilon}}$
$y_i \leftarrow \gamma \hat{x_i} + \beta = BN_{\gamma,\beta}(x_i)$

论文中$\gamma和\beta$是需要学习的仿射参数