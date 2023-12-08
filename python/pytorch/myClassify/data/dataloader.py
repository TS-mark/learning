import torch
from torch.utils.data import DataLoader, Dataset
from torchvision.io import read_image
from torchvision import transforms
import pandas as pd
import os

class PicClsDataset(Dataset):
    """
    预想的目录结构：
    --img_dir
        --cls1
            --****.jpg
            --****.jpg
            ...
        --cls2
            --****.jpg
            --****.jpg
            ...
        --cls3
            ...
    标注的结构：
    --annotations_file
        pic_path 0
        pic_path 0
    否则按照图片文件创建标签文件

    transform:--在线数据增强
    """
    def __init__(self, img_dir, annotations_file = None, transform = None, target_transform = None):
        self.img = img_dir
        self.labels = None
        self.label_mapping = {}
        # 创建标签文件
        if annotations_file is None or not os.path.isfile(annotations_file):        
            with open(os.path.join(img_dir, "annotations.txt"), "w") as f:
                classes = os.listdir(img_dir)
                lbm = -1
                for cls in classes:
                    if not os.path.isdir(os.path.join(os.path.join(img_dir,cls))):
                        continue
                    lbm += 1
                    self.label_mapping[cls] = lbm
                    pics = os.listdir(os.path.join(img_dir,cls))
                    for p in pics:
                        if p.endswith(".jpg") or p.endswith(".png"):
                            temp_p = os.path.join(img_dir, cls, p)
                            f.write(temp_p + " " + str(self.label_mapping[cls]) + "\n")
            annotations_file = os.path.join(img_dir, "annotations.txt")
            with open(os.path.join(img_dir, "label_map.txt"), "w") as f2:
                for k in self.label_mapping:
                    f2.write(k + " " + str(self.label_mapping[k]) + "\n")
        self.label_path = pd.read_csv(annotations_file, sep = " ", header = None)
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.label_path)
        
    
    def __getitem__(self, idx):
        img_path = self.label_path.iloc[idx, 0]
        image = read_image(img_path)
        label = self.label_path.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
        

if __name__ == "__main__":
    dataset = PicClsDataset("E:/dataset/tt100k", transform=transforms.Resize(size=22))
    # img, label = dataset.__getitem__(5)
    # print(img, label)
    train_dataloader = DataLoader(dataset, batch_size = 8, shuffle=True)
    for img, label in enumerate(train_dataloader):
        print(img, label)
        break