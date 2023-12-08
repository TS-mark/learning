# collections
这个模块：提供了一些额外的数据类型和容器
*目录：
    *namedtuple
    *deque
    *Counter
    *defaultdict
    *OrderedDict


---

## nametuple
`namedtuple`是一个工厂函数，用于创建具有命名字段的元组。它可以让您为元组的字段命名，从而使代码更具可读性。例如
```python
from collections import namedtuple

# 创建一个名为 'Point' 的命名元组类型，具有 'x' 和 'y' 两个字段
Point = namedtuple('Point', ['x', 'y'])

p = Point(1, 2)
print(p.x)  # 输出: 1
print(p.y)  # 输出: 2
```


---

## deque
`deque`双端队列，听名字就知道可以高效插入和删除
```python
from collections import deque

dq = deque([1, 2, 3])
dq.append(4)        # 从右侧添加元素
dq.appendleft(0)    # 从左侧添加元素
dq.pop()             # 从右侧删除元素
dq.popleft()         # 从左侧删除元素
``` 


---

## Counter
`Counter`是一种用于计数可哈希对象的容器，可以轻松统计元素的出现次数。

最常见的作用：通过collections获取词频

```python
#例如读取词频为3的字母
from collections import Counter

s = 'leetcode'
res = " "
cipin = Counter(s)
for i,k in enumerate(s):
    if cipin[k] == 3:
        res = k
res 
```

---

## defaultdict
`defaultdict` 是一个字典，在访问不存在的键不会引发KeyError（相对dict）
```python
from collections import defaultdict

# 创建一个默认值为 int 的 defaultdict
d = defaultdict(int)
d['a'] += 1
print(d['a'])  # 输出: 1

# 创建一个默认值为 list 的 defaultdict
d_list = defaultdict(list)
d_list['b'].append(1)
print(d_list['b'])  # 输出: [1]

```
## OrderedDict

`OrderedDict` 是一种有序字典，它会按照元素插入的顺序来迭代元素。与普通字典不同，OrderedDict会记住键值对的顺序。
<font color = "red">这个通过维护一个额外的链表来保持键值对的插入顺序</font>
```python
from collections import OrderedDict

d = OrderedDict()
d['b'] = 2
d['a'] = 1

for key, value in d.items():
    print(key, value)
# 输出: b 2
#      a 1

```