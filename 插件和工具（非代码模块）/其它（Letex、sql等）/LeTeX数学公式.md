## Letex书写数学公式

$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$  
求导这么写:  
\frac{\mathrm{d}f}{\mathrm{d}t}: 
$\frac{\mathrm{d}f}{\mathrm{d}t}$


或者f(x)':$f(x)'$

正文(inline)中的LaTeX公式用```$...$```定义

用```$$...$$```代替```$...$```，则例如\sum的下标会在下面  
对比：
$$\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t$$  
${\sum_{i=0}^N\int_{a}^{b}g(t,i)\text{d}t}$


## 插入希腊字母
|显示|命令|显示|命令|
|---|---|---|---|
|α|\alpha|β|\beta|
|γ|\gamma|δ|\delta|
|ε|\epsilon|ζ|\zeta|
|η|\eta|θ|\theta|
|ι|\iota|κ|\kappa|
|λ|\lambda|μ|\mu|
|ν|\nu|ξ|\xi|
|π|\pi|ρ|\rho|
|σ|\sigma|τ|\tau|
|υ|\upsilon|φ|\phi|
|χ|\chi|ψ|\psi|
|ω|\omega| | 

要大写，则首字母大写就可以例如 $\Sigma$ -->\Sigma  

## letex其他标识
|符号|含义|用法|展示|
|---|---|---|---|
|^|上标|C^2_5|$C^2_5$|
|_|下标|C_2^4|$C_2^4$|
|\vec|矢量|\vec a或\vec {a}|$\vec {a}$|
|\overrightarrow|矢量，可以弄多维，那个箭头长一点|\overrightarrow{xy}|$\overrightarrow{xy}$|
|{}|如果长度大于1，需要用这个|||
|\sum|连加|\sum_{i=0}^N|$\sum_{i=0}^N$|
|\prod|连乘|\prod_{i=0}^n|$\prod_{i=0}^n$|
|\lim|极限|\lim_{x\to 0}|$\lim_{x\to 0}$|
|\int|积分|\int_{a}^{b}|$\int_{a}^{b}$|
|<font color = red>\frac </font>|分式|\frac{a}{b}|$\frac{a}{b}$|
|\sqrt||\sqrt[2]{y}|$\sqrt[2]{y}$|
|{\prime}|一撇|a^{\prime}|$a^{\prime}$|
|\nabla|梯度||$\nabla$|
|\partial|偏导符号|$\frac{ \partial a }{ \partial c }$|$\partial$|
|\cdot|点乘||$\cdot$|
|\times|叉乘||$\times$|
|\div|除||$\div$|
|\exits<br>\forall|存在<br>全量||$\exists$<br>$\forall$|
|\emptyset<br>\infty|空集<br>无穷大||$\emptyset$<br>$\infty$|
|\because<br>\therefore|因为<br>所以||$\because$<br>$\therefore$|
|\le<br>\ge|大于等于<br>小于等于||$\le$<br>$\ge$|
|\cup<br>\cap|交<br>并||$\cup$<br>$\cap$|
|\in<br>\notin|属于<br>不属于||$\in$<br>$\notin$|
|\arrow|箭头|\leftarrow<br>\uparrow|$\leftarrow$<br>$\uparrow$|
|\stackrel{r_1}{\rightarrow}|箭头（也不必须是箭头），但上面有个标识||$\stackrel{r}{\rightarrow}$|
|空格|会被letex语法忽略|\quad <br> "\ "|四个空格 <br>"一个空格"|
|垂直符号|\perp|$\perp$|
|估计（x ba）|\hat{x}|$\hat{x}$|
||\tilde{x}|$\tilde{x}$|
||\bar{x}|$\bar{x}$|

---
## 矩阵
注意，写矩阵的时候不能少了```\\```
$$\begin{matrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{matrix}$$

语法：  
```
\begin{matri x}  
1&0&0\\  
0&1&0\\  
0&0&1\\  
\end{matrix}  
```

矩阵边框

pmatrix ：小括号边框  
bmatrix ：中括号边框  
Bmatrix ：大括号边框  
vmatrix ：单竖线边框  
Vmatrix ：双竖线边框  

```
$$\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{bmatrix}$$
```

$$\begin{bmatrix}
1&0&0\\
0&1&0\\
0&0&1\\
\end{bmatrix}$$

省略元素：  
横省略号：\cdots  
竖省略号：\vdots  
斜省略号：\ddots  

$$\begin{bmatrix}
{a_{11}}&{a_{12}}&{\cdots}&{a_{1n}}\\
{a_{21}}&{a_{22}}&{\cdots}&{a_{2n}}\\
{\vdots}&{\vdots}&{\ddots}&{\vdots}\\
{a_{m1}}&{a_{m2}}&{\cdots}&{a_{mn}}\\
\end{bmatrix}$$

---
## 方程组
需要cases环境：起始、结束处以{cases}声明
举例：
```
$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}
$$
```
展示：
$$\begin{cases}
a_1x+b_1y+c_1z=d_1\\
a_2x+b_2y+c_2z=d_2\\
a_3x+b_3y+c_3z=d_3\\
\end{cases}
$$

---
## 阵列
需要{array}  
对齐方式:逐行声明  l左 c中 r右  
竖线：在声明对齐方式时同时声明
```
$$\begin{array}{c|lll}
{↓}&{a}&{b}&{c}\\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}$$
```
$$\begin{array}{c|lll}
{↓}&{a}&{b}&{c}\\
\hline
{R_1}&{c}&{b}&{a}\\
{R_2}&{b}&{c}&{c}\\
\end{array}$$


---
## 文本类

设置颜色：
```
\textcolor{red/blue/green/black/white/cyan/magenta/yellow}{text}
```