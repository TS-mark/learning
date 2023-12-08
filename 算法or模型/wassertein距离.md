# wasserstein距离
Wasserstein距离也是用来度量两个概率分布之间差异的方法，它满足“距离”所需要的三个条件，所以我们称之为“距离”！它有很多别名，比如 optimal transport（简称OT）、Earth Move Distance（简称EMD）。它的思想于1781年被法国数学家 Gasoard Monge 在交通理论中被首次提出。

**主要用于gan网络中**

## 原理大致说明
假定把概率分布p(x)转变成q(x)，设距离函数（可以认为是转移成本）是d(x,y)，则wasserstein距离为：