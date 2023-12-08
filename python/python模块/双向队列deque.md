# collections.deque()

```python
import collections
d = collections.deque([])
d.append('a')
d.appendleft("b")
d.extend(["c","d"]) #最右边添加元素
d.pop()
d.popleft()
d.count("a") # a元素个数
d.remove("c")
```