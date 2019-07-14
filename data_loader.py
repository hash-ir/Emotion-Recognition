from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import transform
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

class FERDataset(Dataset):

    def __init__(self, csv_file, usage, transform=None):
        self.data_frame = pd.read_csv(csv_file)
        self.usage_frame = self.data_frame.loc[self.data_frame['Usage'] == usage]
        self.usage_frame.reset_index(drop=True, inplace=True)
        self.transform = transform

    def __len__(self):
        return len(self.usage_frame)

    def __getitem__(self, idx):
        image = self.usage_frame.loc[idx, 'pixels']
        label = self.usage_frame.loc[idx, 'emotion']
        image = np.array([int(item) for item in image.split(' ')]).reshape(-1, 48, 48).astype(np.uint8)
        sample = {}
        sample['image'] = image
        sample['label'] = label
        
        if self.transform:
            sample = self.transform(sample)

        return sample

# data_transforms = transforms.Compose([
#     transform.Normalize(),
#     transform.ToTensor()
# ])

# train = FERDataset('fer2013.csv', 'Training', transform=data_transforms)
# bs = 16
# train_loader = DataLoader(train, batch_size=bs, shuffle=True)

# for idx, sample in enumerate(train_loader):
#     print(idx, sample)
#     if idx == 2:
#         break

