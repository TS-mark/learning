# TargetEncoding
---

大概把这个算法模型看懂了，先上代码：

```python

from category_encoders import *
import pandas as pd
from sklearn.datasets import load_boston
bunch = load_boston()
y = bunch.target
X = pd.DataFrame(bunch.data, columns=bunch.feature_names)
enc = TargetEncoder(cols=['CHAS', 'RAD'],min_samples_leaf = 100,smoothing = 2).fit(X, y)
numeric_dataset = enc.transform(X)
# print(numeric_dataset.info())

```

相当于训练一次类别函数。
### 调参侠必备：
* min_samples_leaf：计算类别平均值时的最小样本数（即若该类别出现次数少，则将被忽略），用以控制过拟合-->避免数量很少的量分为一类，与样本量有关的；
* smoothing：平衡分类平均值与先验平均值的平滑系数。其值越高，则正则化越强；-->默认为1，这个值等于min_samples_leaf时感觉就跟没有一样
′ 是类别特征X中类别为k的编码值

### 代码稍微解释下：  
* TargetEncoder 相当于一次训练了。  
* enc，训练的模型结果  
* enc.transform(X): 把x中指定的cols转换为目标编码  
### 值解释一下：  
* 最后被代替的类别，就是波动在样本标签的均值（y.mean())，这个分类的结果受y值标签的影响  