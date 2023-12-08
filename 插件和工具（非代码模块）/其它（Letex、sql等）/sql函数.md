# sql常用函数

| 函数名 | 函数功能 | 函数用法 |
| --- | - | --- |
|cast(字段名 as string)|修改数据类型|字段名改为string类型|
|NVL(E1, E2)|代替e1空值 | 如果 E1 为空，则用 E2 代替|
|NVL2(E1, E2, E3)|跟上面类似|如果e1为空，输出e2，否则输出e3（原来的值就没了）|
|regexp_replace(date,'-',''))| 正则表达式| 将date字段中'-'替换为''|
|substr(startIndex, length)<br>substring(startIndex, endIndex)|截取字符串|substr，第二个参数是长度<br>substring第二个参数是最后一位的index|
|substring_index(str, delim, count)|||
|row_number()/rank()/dense_rank() <br>over(partition by A order by B asc/desc)|排序，得到排名,以A字段分区，b字段排序|rank()（1，2，2，4）<br>dense_rank()(1,2,2,3)<br>row_number()(1,2,3,4)|
|concat(a,b)<br>concat_ws(str,a,b)|将ab字符串拼接|ab中间加了一个"-"|
|split(str, regex)|拆分字符串|取某一项：split(id,',')[0]|
|datediff(a.dt,"2021-08-20")|计算日期差|dt-20200820|
|collection_set<br>collection_list|跟group和着用的|select username, collect_list(video_name)[0] from t_visit_video group by username|

## 根据某个字段合并
用到函数(collect_set、collect_list)  
```sql
select subtype
,concat_ws('&',collect_set(case(a as string))) a
from table
group by subtype
```
将subtype字段中所有a字段合并为一个，这两个函数的set和list跟python逻辑相同


## sql比较厉害的查询

1.查询两个表不一样的部分
```sql
select * from B where (select count(1) from A where A.ID = B.ID) = 0
```
以上是mysql版本，hive版本
```sql
select a.* FROM A a left outer join B b on a.qq = b.qq
WHERE b.qq is null;
```