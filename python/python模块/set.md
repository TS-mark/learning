# set(哈希表)
---
对于set而言，主要有两种用法

## set用法、函数汇总
|用法|解释|
|---|---|
|x&y|x集合和y集合交集|
|x\|y|并集|
|x-y|差集|
|x^y|补集，简单理解就是并集-交集|
|x.add()|向集合x增加元素|
|x.remove(element)|移除元素element|


### 遍历set
```python
weekdays = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
 
for d in weekdays:
    print (d)
```