##  1、基本思想
（1）将之前所有层的输出特征连接起来，作为下一层的输入，最大化 cardinality（分支路径的数量）。

（2）由梯度信息结合的思想，让高 cardinality 和稀疏连接来提升网络的学习能力。


3.3 其他改进
为了适合单GPU训练，做了额外的设计和仿真设计

新的数据增强方法：Mosaic和Self-Adversarial Training(SAT)
应用遗传算法选择最优的超参数
修改现有方法，更利于训练和检测： modifified SAM, modifified PAN, and Cross mini-Batch Normalization (CmBN)
