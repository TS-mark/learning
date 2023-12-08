from torchvision.datasets import MNIST
import torchvision.transforms as transforms
from torch.utils.data import DataLoader

data_train = MNIST("./data",
                    download=False,
                    transform = transforms.Compose([
                       transforms.Resize((32,32)),
                       transforms.ToTensor()])
                   )
data_test = MNIST("./data",
                    train = False, 
                    download = False,
                    transform = transforms.Compose([
                       transforms.Resize((32,32)),
                       transforms.ToTensor()])
                   )
data_train_loader = DataLoader(data_train, batch_size=256,
                               shuffle=True, num_workers=2)
data_test_loader = DataLoader(data_test, batch_size = 1024,
                              num_workers=2)
