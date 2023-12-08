# python

|函数|例子|解释|
|---|---|---|
|str.join(str)|  ||
|str.format()|"网站名：{name}, 地址 {url}".format(name="菜鸟教程", url="www.runoob.com")||
||"{1} {0} {1}".format("hello", "world")  # 设置指定位置|字符串格式化输出|

## 列表、numpy、dataframe计数
``` python
from collections import Counter
Counter(list\pandas\numpy )
```ist特定元素下标：
```python
a=[72, 56, 76, 84, 80, 88]
print(a.index(76))
```
## list特定位置插入insert(下标, 元素)
```python
a=[72, 56, 76, 84, 80, 88]
print(a.insert(2,74))
# a = [72, 56, 74, 76, 84, 80, 88]
```
---

## apply函数 用法

```python
# 将data的所有列转换为数字类型（int、float）
data = data.apply(pd.to_numeric)
# 或者
data.c3 = data.c3.astype("float")

```


--- 

## collections.deque()
deque是一个 **双端队列**，如果经常需要在两端append数据时使用这个方法
```python
from collections import deque 
d = deque([])
d.append("a")
d.appendleft("b")
d.extend(['e','f'])
d.pop()
d.popleft()
d.rotate( -2 ) # 正数旋转两个位置（有需要自己调试）
d.remove("c") # 移除c
d.reverse()

e = deque(maxlen = 5) # 如果超过五个元素，则原来数组中元素会被挤出
```

## 堆排序

```python
# 大顶堆
from heapq import *
def heap_sort(nums):
    temp_res = []
    res = []
    for i in nums:
        heappush(temp_res, -i)
    while(temp_res):
        res.append((-1)*heappop(temp_res))
```