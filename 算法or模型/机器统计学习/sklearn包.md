# sklearn

---

## 加载示例数据集

```python
from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()
```
## 学习&预测 
---
### 设置参数
这里的参数可以手动设置，但是最好用网格搜索和交叉验证设置，自动找到合适参数值。

估计器命名为 **clf** ，因为他是分类器（classifier）

```python
from sklearn import svm
clf = svm.SVC(gamma = 0.001, c = 100.)
```

### 学习
```python
clf.fit(X_train, y_train)
```

### 预测
```python
clf.predict(X_test)

```

## 模型持久化
使用python内置持久化模块（pickle）保存模型
```python
import pickle
s = pickle.dumps(clf)
clf2 = pickle.loads(s)
clf2.predict(X[0:1])
```
以上最好别用，用joblib可以序列化到磁盘，而不是变量
```python
from sklearn.externals import joblib
joblib.dump(clf, 'filename.pkl') # 存储模型

clf = joblib.load('filename.pkl') # 加载模型
"""然后就predict吧"""
```

### 再次训练&更新参数

估计器的超参数可以通过 **sklearn.pipeline.Pipeline.set_params** 方法在实例化之后进行更新。 调用 fit() 多次将覆盖以前的 fit() 所学到的参数:

```python
clf = SVC()
clf.set_params(kernel='linear').fit(X, y)
clf.set_params(kernel='rbf').fit(X, y) 
```

### 多分类与多标签拟合

当使用 多类分类器 时，执行的学习和预测任务取决于参与训练的目标数据的格式:
```python
>>> from sklearn.svm import SVC
>>> from sklearn.multiclass import OneVsRestClassifier
>>> from sklearn.preprocessing import LabelBinarizer

>>> X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
>>> y = [0, 0, 1, 1, 2]

>>> classif = OneVsRestClassifier(estimator=SVC(random_state=0))
>>> classif.fit(X, y).predict(X)
array([0, 0, 1, 1, 2])

>>> y = LabelBinarizer().fit_transform(y)
>>> classif.fit(X, y).predict(X)
array([[1, 0, 0],
 [1, 0, 0],
 [0, 1, 0],
 [0, 0, 0],
 [0, 0, 0]])
```
