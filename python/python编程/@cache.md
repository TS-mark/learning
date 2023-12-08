# @cache

### 首先抛砖引玉，看这么一个问题：

leetcode397 整数替换

给定一个正整数 n ，你可以做如下操作：

如果 n 是偶数，则用 n / 2替换 n 。  
如果 n 是奇数，则可以用 n + 1或n - 1替换 n 。  
返回 n 变为 1 所需的 最小替换次数 。  

再看这个问题的两个python代码求解：
```python
class Solution:
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n%2 == 1:
            return min(self.integerReplacement((n+1)//2), self.integerReplacement((n-1)//2)) + 2
        else:
            return self.integerReplacement(n//2) + 1
```
```
Accepted
47/47 cases passed <font color = "red">(144 ms)</font>
Your runtime beats 35.13 % of python3 submissions
Your memory usage beats 53.33 % of python3 submissions (15.9 MB)
```
再看下面这个:
```python
class Solution:
    @cache
    def integerReplacement(self, n: int) -> int:
        if n == 1:
            return 0
        if n%2 == 1:
            return min(self.integerReplacement((n+1)//2), self.integerReplacement((n-1)//2)) + 2
        else:
            return self.integerReplacement(n//2) + 1

```
```
Accepted
47/47 cases passed <font color = "red">(48 ms)</font>
Your runtime beats 54.36 % of python3 submissions
Your memory usage beats 40 % of python3 submissions (16 MB)
```

 可以看到整段代码中就多了一个@cache，所以cache到底是什么东西？

---

## cache

cache常用于需要递归的函数中
摘自

1.链接：https://www.jianshu.com/p/9e57e1db2297
2.链接：https://blog.csdn.net/weixin_43790276/article/details/130115410


Python 内置模块 functools 提供的高阶函数 @functools.cache 是简单轻量级无长度限制的函数缓存，这种缓存有时称为 "memoize"（记忆化）。它是 3.9 新版功能，是在 lru_cache 缓存基础上简化了的对无限长度缓存。

官方例：
```python
from functools import cache 

@cache
def factorial(n):
    return n * factorial(n-1) if n else 1
```

缓存机制是LRU（最久未使用）  
lru_cache() 使用了 LRU（Least Recently Used）最久未使用算法，这也是函数名中有 lru 三个字母的原因。最久未使用算法的机制是，假设一个数据在最近一段时间没有被访问到，那么在将来它被访问的可能性也很小， LRU算法选择将最近最少使用的数据淘汰，保留那些经常被使用的数据。  
cache() 是在Python3.9版本新增的，lru_cache() 是在Python3.2版本新增的， cache() 在 lru_cache() 的基础上取消了缓存数量的限制，其实跟技术进步、硬件性能的大幅提升有关，cache() 和 lru_cache() 只是同一个功能的不同版本。

lru_cache() 本质上是一个为函数提供缓存功能的装饰器，缓存 maxsize 组传入参数，在下次以相同参数调用函数时直接返回上一次的结果，用以节约高开销或高I/O函数的调用时间。