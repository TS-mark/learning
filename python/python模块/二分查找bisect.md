## 查找

```python
import bisect
a = [0， 0， 1， 1， 1， 2， 2]
bisect.bisect(a,1) #输出5，大于1的那个值的索引
bisect.bisect_left(a,1) #输出2，小于等于1的那个值的索引
```
## 插入
```python
import bisect
a = [0, 1, 2, 4]
bisect.insort(a,3) #向a插入3，3这个东西不能是list
a #变成了[0, 1, 2, 3, 4]，顺序插入
```
