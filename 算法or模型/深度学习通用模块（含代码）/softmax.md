# softmax和log_softmax

$$softmax(z_i) = \frac{\exp(z_i)}{\sum_j \exp(z_j)}$$

softmax有两个意外情况：
* 上溢出：$z_j$极大
* 下溢出：$z_j$为负数且绝对值很大，在计算时$ \sum_j \exp(z_j) $被四舍五入为0 

----
解决上溢出：
c = max(z)
$\log (softmax(z_i)) = \log(\frac{exp(z_i-c)}{\sum_j exp (z_j - c)})$

解决下溢出：

$\log (softmax(z_i)) = {exp(z_i-c)}-\log({\sum_j exp (z_j - c)})$