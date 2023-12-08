import torch
import torchvision
import torchkeras
from torch import nn
from torch.utils.data import Dataset,DataLoader
from torchvision import transforms as T
from torchvision import datasets

print("torch.__version__ = ", torch.__version__)
print("torchvision.__version__ = ", torchvision.__version__)
print("torchkeras.__version__ = ", torchkeras.__version__)


transform_img = T.Compose(
    [T.ToTensor()])

def transform_label(x):
    return torch.tensor([x]).float()