## 先查看存在的docker镜像
### 流程：
1. 查看docker镜像id
2. 暂停docker容器
3. 删除docker容器
这三步对应的代码：

```bash
docker ps -a

docker stop 容器id

docker rm 容器id
```