## 好家伙
----
leetcode 743

----
```python

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        a = [[10000000 for _ in range(n+1)] for _ in range(n+1)]
        for i in range(n+1):
            a[i][i] = 0
        #初始化
        for i in range(len(times)):
            a[times[i][0]][times[i][1]] = times[i][2]
        for km in range(1,n+1):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    a[i][j] = a[i][km]+ a[km][j] if a[i][km]+ a[km][j] < a[i][j] else a[i][j]
        res = -1
        print(a)
        for i in range(1,n+1):
            if k == i :
                continue
            if a[k][i] == 10000000:
                return -1
            else:
                res = max(a[k][i],res)
        return res
```