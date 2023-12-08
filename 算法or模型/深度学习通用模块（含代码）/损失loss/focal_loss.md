# focal loss
---
focal loss 主要是为了解决one-stage目标检测中正负样本数量极不平衡的问题。


### Cross Entropy Loss:二分类交叉熵损失 
其中y取值为1和-1，代表前景和背景，p取值为0-1，为前景概率
$$
CE(p,y)=\begin{cases}
-log(p)   \quad\quad\quad  y=1\\
-log(1-p) \quad  otherwise\\
\end{cases}
$$
转换为$p_t$,公式化后：
$$CE(p,y) = CE(pt) = -log(pt)$$
### BCE(balanced cross entropy)
常见解决类不平衡的方法，引入权重因子$\alpha$
$$CE(p,y) = CE(pt) = -\alpha_t log(pt)$$  
### Focal Loss  
修改为调制因子$(1-p_t)^\gamma$  
$$FL(p_t) = -(1-p_t)^\gamma log(p_t)$$


---
### 对比FL和CE
![](./img/focalloss.png)