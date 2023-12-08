# docker上搭建jupyter notebook
*保底需求*：docker上有python,有jupyter notebook


---

启动容器：
一个是远程连接的22端口，一个是jupyter映射的4439端口，剩下的参数参考[3.容器ssh配置](3.%20%E5%AE%B9%E5%99%A8SSH%E9%85%8D%E7%BD%AE.md)
```bash
docker run -itv /home/zhang.wenzhao1/markzhang:/home/markzhang:rw --gpus "all" --shm-size 32g -p 4438:22 -p 4439:4439 --name zwz_common_train 67860d807b50
```

剩下的操作参考[知乎这个文章](https://zhuanlan.zhihu.com/p/612188740?utm_id=0)。
```
# 初始化jupyter_notebook_config.py
$ jupyter notebook --generate-config
 
# 生成密钥
$ ipython
[1]:from notebook.auth import passwd
[2]:passwd()
Enter password: XXXX
Verify password: XXXX
Out[2]: '生成的一串密钥'
# 注意保存生成的密钥  

exit #退出生成密钥
```
修改jupyter_notebook_config.py配置文件
```
# 编辑jupyter_notebook_config.py
# 如果你不知道jupyter_notebook_config.py，可以使用find命令找一下
$ vim /root/.jupyter/jupyter_notebook_config.py
 
# 设置c.NotebookApp.password，注意前面加 u
c.NotebookApp.password=u'生成的一串密钥'
 
## 设置外部访问
# 连通性设置
c.NotebookApp.allow_remote_access = True

# ip设置
c.NotebookApp.ip='*'  # 自动获取服务器ip

# 打开root权限启动
c.NotebookApp.allow_root =True

# 禁止自动打开浏览器
c.NotebookApp.open_browser = False

# 端口设置
c.NotebookApp.port = 4439  # 创建docker时候配置的端口号
 
# 启动jupyter notebook
$ jupyter notebook
```
就ok了。