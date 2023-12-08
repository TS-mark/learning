# random模块
```python
import random
```
|函数名|用法|功能|
||random.random()|产生0-1之间浮点数|
||random.randint(1, 10)|产生1-10的整数|
||random.uniform(1.1, 5.4)|产生1.1-5.4的浮点数|
||random.choice("asdfgasdfasf")|从序列中随机选取一个元素|
||random.randrange(1, 100, 2)|生成间隔为2，1-100之间的一个随机整数|
||random.shuffle(a)|将序列a打乱|
|sample|random.sample([i for i in range(3000)], 6)|从0-2999中随机采样6个数|