argparse是对命令行解析的

具体用法参考argparse_test.py
```python
## 创建解析对象
parser = argparse.ArgumentParser(description = "you script description")
## 向对象中添加命令行参数和选项
parser.add_argument('--epochs', type = int, default = 30)
parser.add_argument("--batch", type = int, default = 50)
## 进行解析
args = parser.parse_args()

epochs = args.epochs
batch = args.batch
```
命令行输入:

```bash
python test.py 30 50
# 或者
python test.py --epochs 30 --batch 50
```