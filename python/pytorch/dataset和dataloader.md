# dataset 和 dataloader使用

---
## dataset
dataset这个函数生成单一样本以及其对应标签。  
自己构建的dataset类必须继承Dataset类中的三个函数：`__init__, __len__, __getitem__`
```python
from torch.utils.data import Dataset
from torchvision.io import read_image

#其中transform是对标签的处理
class CustomerDataset(Dataset):
    def __init(self, annotations_file, img_dir, transform = None, target_transform = None):
        self.img_labels = pd.read_csv(annnotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform
    
    # 数据集总大小
    def __len__(self):
        return len(self.img_labels)
    
    # 获取图片及其对应label
    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```


## dataloader  
dataloader生成的是批样本，根据dataset中的样本以及对应标签。
批训练优点：训练效率更高，使模型抗噪能力更好  
dataloader在每次训练后打乱shuffle，还可以使用python多进程能力（multiprocessing）加速训练
```python
Dataloader(dataset:Dataset, \
    batch_size:int, \
    num_workers:int, # 取决于cpu个数\
    shuffle:bool, \
    pin_memory:bool, # 将tensor保存到gpu中，好坏对于效率影响未知\
    drop_last:bool, # 如果样本数不是batch_size的整数倍，把最后一批次丢掉\
    timeout:float, \
    sampler:Union[Sampler, Iterable], #如何对数据采样，可以使用默认，也可以自己实现\
    prefetch_factor:int, \
    collate_fn: Optional[_collate_fn_t], # 对一个batch的数据进行处理，处理成一个batch， 例如transform归一化\
    _iterator:Optional['_BaseDataLoaderIter'], \
    __initialized=False
    )

```

实际案例
```python
from torch.utils.data import Dataloader

train_dataloader = DataLoader(training_data, batch_size = 64, shuffle = True)
test_dataloader = Dataloader(test_dataset, batch_size = 64, shuffle = True)
```
调用dataloader
```python
train_features, train_labels = next(iter(train_dataloader))
# 实际得到一个64维的标签和特征
print(f"Feature batch shape: {train_features.size()}") # 64, 1, 28, 28
print(f"Feature batch shape: {train_labels.size()}") # 64
```