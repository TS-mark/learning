# stable diffusion

## 模型结构&学习：待补充
![](./img/stable%20diffusion1.png)
生成的\e过程中不断地增加噪声

### UNet
### clip --> 
输出：77个嵌入项链，每个向量有768个维度。

### Txt2Img/Img2Img

### LoRA（low-rank
微调训练，新增参数->pre train和新数据

## stable diffusion推理过程
### prompt
### 若干次采样
### 进行解码
t


#### 基本工具：diffusers库-》hugging face
#### SD Webui -> github这就是个ui界面了
输入：
1. 提示词prompt
2. 反向提示词 （nsfw，extra arms，low quality）
3. 采样方法（DPM++）
4. 迭代步数（steps）
5. 相关性
6. 随机种子
7. 