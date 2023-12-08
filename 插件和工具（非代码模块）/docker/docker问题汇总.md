```bash
docker run -itv /home/zhang.wenzhao1/markzhang:/home/markzhang:rw --gpus "device=4" --shm-size 32g -p 8001:22 --name zwz 容器代码 /bin/bash
```

其中shm-size 32g这个参数加上去，主要是为了解决报错：
```python
RuntimeError: DataLoader worker (pid 5675) is killed by signal: Bus error. It is possible that dataloader's workers are out of shared memory. Please try to raise your shared memory limit.
```  
和 
```python  
RuntimeError: unable to write to file </torch_4823_1309448367_1>: No space left on device (28)
ERROR: Unexpected bus error encountered in worker. This might be caused by insufficient shared memory (shm).
ERROR: Unexpected bus error encountered in worker. This might be caused by insufficient shared memory (shm).
```