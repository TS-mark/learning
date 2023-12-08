# importlib 
这个库主要是用来代替`import`的，跟`import`用法很像。
基本上用法也就是`importlib.import_module("..")`


```python
import importlib

# 与 import time 效果一样
time = importlib.import_module('time')
print(time.time())

# 与 import os.path as path 效果一样
path = importlib.import_module('os.path')
path.join('a', 'b')  # results: 'a/b'

# 相对引入, 一级目录，与 import os.path as path 效果一样
path = importlib.import_module('.path', package='os')
path.join('a', 'b')  # results: 'a/b'

# 相对引入，二级目录，与 import os.path as path 效果一样
path = importlib.import_module('..path', package='os.time')
path.join('a', 'b')  # results: 'a/b'
```
可以通过
```python
def run(model_name, input):
    if model_name == 'resnet_50':
        from resnet_50.model import load_model
    elif model_name == 'hrnet':
        from hrnet.model import load_model
    elif model_name == 'moblienet':
        from mobilenet.model import load_model

    model = load_model()
    output = model(input)
    return output

```
