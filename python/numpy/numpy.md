np.linalg.norm
linalg=linear（线性）+algebra（代数），norm则表示范数。
```python
x_norm=np.linalg.norm(x, ord=None, axis=None, keepdims=False)
```
|参数|含义|取值|
|---|---|---|
|x|向量数据||
|ord|范数类型（默认二范数）|ord = 1  一范数：绝对值和<br>ord = 2  二范数：平方开方<br>ord = np.inf  无穷范数(max(|x_i|))<br>|
|矩阵|||
|ord||ord = 1:列和的最大值，ord = 2 求特征值，然后求最大特征值的算术平方根|
|axis||axis = 1表示按行处理<br>axis = 0 按列处理|
|keepdims|是否保持矩阵的二维特性|True为保持，默认false|

---
```python
np.random.random([100, 50])
```
上方代表生成100行 50列的随机浮点数，浮点数范围 : (0,1)