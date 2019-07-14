import torch
import numpy as np
import torchvision.transforms.functional as F
from PIL import Image

class Resize(object):
    def __init__(self, size):
        self.size = size
    
    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        image = F.to_pil_image(image)
        # image = Image.fromarray(image)
        # resize = transforms.Resize(self.size)
        # image = resize(image)
        image = F.resize(image, self.size)

        return {'image': np.array(image), 'label': label}

class Normalize(object):
    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        image = np.true_divide(image, 255)

        return {'image': image, 'label': label}

class Gray2RGB(object):
    def __call__(self, sample):
        image, label = sample['image'], sample['label']
        image = np.repeat(image, 3, axis=0)

        return {'image': image, 'label': label}

class ToTensor(object):
    def __call__(self, sample):
        image, label = sample['image'], sample['label']

        return {'image': torch.from_numpy(image),
                'label': torch.from_numpy(np.array([label]))}