## 随机采样
主要就是order by rand()


```sql
limit 2,1
--- 筛选第三名（第一个数字表示除了前几个，第二个数字表示筛选几个值）
```


```sql
select * from table_a order by rand() limit 100
```

## 计算一个表中相同的两项的时间差

1. 首先，计算时间排名(row_number)
```sql
   create table 表_mid as
   select 
   user_id,
   time,
   row_number() over (partition by user_id order by time desc)  as time_rank
   from 表a
```

2. 计算表的时间差
```sql
    select 
    a.user_id,
    a.time -- 筛选最大的日期
    from 
    表_mid a
    join
    表_mid b
    on a.time_rank = b.time_rank + 1 and a.user_id = b.user_id
```
