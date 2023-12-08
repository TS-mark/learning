# docker windows:


----
## 注：测试由于windows虚拟机没有硬件虚拟化功能，daemon无法使用。  

步骤：  
1. 开启虚拟化  
    * 控制面板 -> 程序和功能 -> 启动或关闭Windows功能 -> 勾选 ->适用于linux的Windows子系统
    * 
2. 安装wsl2
    * 查看:[官网](https://learn.microsoft.com/zh-cn/windows/wsl/install-manual#step-3---enable-virtual-machine-feature)
    * 安装好后输入wsl --set-version ubuntu-18.04 2
    将ubuntu wsl设置成wsl2  
    其他可能用到的操作：
    ```bash
    wsl --set-version ubuntu-18.04 2
    wsl -l -v
    bcdedit /set hypervisorlaunchtype auto
    wsl --shutdown
    ```

3. 安装docker desktop 
    * powershell运行
    ```bash
    Enable-WindowsOptionalFeature -Online -FeatureName Microsoft-Hyper-V -All
    ```
    * 重启电脑了


4. 安装完成后
查看是否安装完成的指令：
输入  
```bash
docker version
```

```bash
docker run hello-world
```

```bash
# 查看镜像
docker images
```

其他操作：[更新wsl的apt源](https://blog.csdn.net/weixin_41529012/article/details/117226884)  
如果下载完wsl2仍然无法使用