# git使用到的

---

## 配置SSH
注册git：我看的这个[博客](https://blog.csdn.net/lala_yanzi/article/details/124962662)
大致说明下，打开git bash
输入
```git
@p配置用户名
git config --global user.name "你的用户名"
@配置邮箱
git config --global user.email "你的邮箱"
@生成密钥（输入后几次enter结束）
ssh-keygen -t rsa -C “你的邮箱”

@配置ssh变量
git config --global ssh.variant ssh
```
打开文件夹  
*  windows：C:\users\"username"\.ssh  
  
复制其中id_rsa.pub文件内容（公钥）  
登录gitlab，在“setting”中添加ssh key  

*  ubuntu:  ~/.ssh
`cat ~/.ssh/id_rsa.pub`


![](https://img-blog.csdnimg.cn/ab440da73617464cad1d09a80d38277d.png)

公钥就配置成功了

## 远程仓库连接
```git
git remote
```

## 切换\创建分支
切换
```git
git checkout -b branch名
```
以上等价于：`
```git
git branch branch名
git checkout branch名
```

创建

## 上传

上传git必须在含有.git的文件目录下

```git
git clone -b 分支名 http的git路径
# 或者
git pull origin 分支名

# 加入暂存区 add .
git add .

# 提交到仓库commit，-m 后增加注释信息
git commit -m "注释信息"

# 以上两步在修改文件的时候也可以用 commit -a来代替
git commit -am "修改巴拉啦文件"

# git push origin 分支名
```

## git初始化仓库并同步到远程

```git
git init
```
可以通过git status命令查看当前git仓库状态


```
git remote add origin https://github.com/TS-mark/learningdocument.git
```
## 处理关于git中linux和windows不同步问题

如果是windows使用git add 会有警告：
`Git: ‘LF will be replaced by CRLF the next time Git touches it‘`

原因：
Dos/Windows平台默认换行符：回车（CR）+换行（LF），即’\r\n’  
Mac/Linux平台默认换行符：换行（LF），即’\n’  
企业服务器一般都是Linux系统进行管理，所以会有替换换行符的需求  
```bash
#提交时转换为LF，检出时转换为CRLF
git config --global core.autocrlf true
```