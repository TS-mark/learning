# pandas Dataframe巧用？
---

### （说白了还不是应付面试）

# pandas.DataFrame

|函数|例子|解释|
|---|---|---|
|replace|df.replace("a", "b", inplace = True)|把df中的a替换成b，并改变数据源|
||df.c1.replace({"a":"aa","e":"ee"})|df中c1列所有a替换成aa，e替换成ee（这是一个多替换的操作）|
|copy|df1 = df2['a'].copy()|dataframe深拷贝，df2转移到df1|
|loc(获取行)|df.loc["ind"]|获取index为"ind"的行|
|啥也没有直接获取列|df["col"]|获取columns为"col"的列|
|loc(获取具体值)|df.loc["ind","col"]|获取df index、columns|
||df["col"]["BeiJing"]|等同于上函数|
|isin|df["E"].isin(["11","22"])|如果df["E"]中有11和22，是True,否则False|
|T|df.T|将df转置|
|sort_values|df.sort_values(by="gdp", ascending=True)|按"gdp"列排序，递增排序|
|sort_index|df.sort_index(ascending=True,inplace = True)|列排序|
|count|df.count()|非空个数|
|sum|df.sum()||
|min \ max|df.max(axis = 0)|返回每列最大值（axis默认0）|
|idxmax|df.idxmax()|返回最大值的index|
|mean \ var \ std \ median \ mode |没啥说的median中位数、mode众数||
|quantile|df.quantile(0.75)|75分位数|
|corr|协方差||
|dropna|dropna(axis = ?, inplace = ?)|删除空行|
||data.dropna(axis = 0, subset = ["Age","sex"])|丢弃‘Age’和‘Sex’这两列中有缺失值的行|
|drop|data.drop(["c1#i","c2#b"],  axis = 1, inplace = True)|删除data的列|
|fillna|fillna(value = 5)|用5代替空值|
|rank|df.rank(method = "min")|最小值排第一，如果遇见重复值，排名是一样的|
||df.rank(method = "first")|输出与min一样，遇见重复值，第一个出现的排名高|
||df.rank(method = "max")|最大值排第一|
||df.rank(method = "average")|输出与min一样，重复值的输出是一个均值，如果method缺省， **average** 是默认值|
|join|DataFrame.join(other, on=None, how=’left’, lsuffix=”, rsuffix=”, sort=False)|通过索引或者指定的列连接两个DataFrame。|
|sort_values|DataFrame.sort_values(by, axis=0, ascending=True, inplace=False, kind=’quicksort’, na_position=’last’)|by 排序的列 <br>axis：1是columns，默认0<br>ascending:升序或者降序<br>inplace：是否替换<br>kind：选择排序算法（quicksort、mergesort、heapsort）<br>na_posision：空值摆放次序，默认last最后（first）|
|astype|ndata = ndata.series名.astype("float")|更改series的属性|
|pd.to_numeric|x = x.apply(pd.to_numeric)|高效转换所有数据类型|
|drop_duplicates|ndata.drop_duplicates(subset=['tal_id','xh_id'],keep='first',inplace=True)|去重|
|value_counts()|df[].value_counts()|统计词频|

```python
a = [1,2,3,4,5]
b = [6,7,8,9,10]
```


|写法|解释|
|---|---|
|pd.DataFrame([a, b])|可以这么写|
|pd.DataFrame({"a":a, "b":b})|可以这么写，字典索引|
|df.values|返回numpy数组|
|df.index||
|df.columns||
|df.shape||
|df.size||
|df.dtypes|展示df所有列的数据类型|
|一系列都是行切片||
|df["ind1": "ind6"]|行切片|
|df.loc["ind1": "ind6"]|行切片|
|df.iloc[0: 5]|行切片|
|下面是列切片||
|df.loc[:, "col1": "col10"]|列切片|
|df.iloc[:, 0: 9]|列切片|
|索引||
|df[df > 0]||
|df[df.col1 >0]||
|||
|df.head(5)||
|df.query|筛选出某些列值符合要求的行数据,例如df.query("col == x"),等价于df[df[col] == x]|


### dataframe聚合




```python
import pandas as pd
 
df = pd.DataFrame({'gender' : ['男', '女', '男', '男', '男', '男', '女', '女', '女'],
          'name' : ['周杰伦', '蔡依林', '林俊杰', '周杰伦', '林俊杰', '周杰伦', '田馥甄', '蔡依林', '田馥甄'],
          'income' : [4.5, 2.9, 3.8, 3.7, 4.0, 4.1, 1.9, 4.1, 3.2],
         'expenditure' : [1.5, 1.9, 2.8, 1.7, 4.1, 2.5, 1.1, 3.4, 1.2]
         })
```
结果：
![](dataframe1.png)

## 所求目标：
---
（我不知道为啥这个表这么多重复列不过不重要）

每个人中收入最高的数据

```python
def head_1(series):
    return series.sort_values(by = "income", ascending = False).head(1)

df.groupby(by = ["name","gender"],axis = 0).apply(head_1)
```
结果：
![](dataframe2.png)

如果看这个结果中出现两次gender和name不爽，就drop掉他们

```python
df.groupby(by = ["name","gender"],axis = 0).apply(head_1).drop(["gender","name"], axis = 1)
```
![drop掉他们了](dataframe3.png)

其他写法，比较牛逼的
```python
df.sort_values(by = ["income"],ascending = False).groupby(by = ["name","gender"],axis = 0).head(1)
```
这个写法，如果sort_values 在groupby之后，会被提示用apply，这也是为啥之前首先就apply了（我还是觉得这个写法强大）


```python
df.groupby(by = ["name","gender"],axis = 0).max()
```
这个写法在输出每个属性前2的值的时候肯定是不行的。

---

## 随机采样

```python
DataFrame.sample(n=None, frac=None, replace=False, weights=None, random_state=None, axis=None)
```

n： 要抽取的行数,需为整数值  
frac：抽取的比列,需为小数值，比方说我们想随机抽取30%的数据，则设置frac=0.3即可。  
replace：抽样后的数据是否代替原DataFrame()，默认为False  
weights：默认为等概率加权  
random_state：随机种子，本质是一个控制器，设置此值为任意实数，则每次随机的结果是一样的  
axis：抽取数据的行还是列，axis=0的时是抽取行，axis=1时是抽取列
 经过测试检验发现，如果两个相同行数的dataframe，这两个dataframe在选取<font color = "red">相同</font>的random_state后，随机采样结果的index是<font color = "red">相同</font>的

 ## 删除重复项
 
 ```python
data.drop_duplicates(subset=['A','B'],keep='first',inplace=True)
 ```

```python

```