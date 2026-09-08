import os
import time
import io

import numpy as np

import torch
import torch.nn as nn
import torch.nn.functional as F

from torch.utils.data import Dataset
from torch.utils.data import DataLoader
from torch.utils.data.dataset import Subset
from torchvision.models import resnet101

from torchvision import datasets
from torchvision import transforms

import time

if torch.cuda.is_available():
    torch.backends.cudnn.deterministic = True

# Hyperparameters
RANDOM_SEED = 1
LEARNING_RATE = 0.01
NUM_EPOCHS = 50
DATA_ROOT = "data"
NUM_CLASSES = 10
BATCH_SIZE = 128
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')

def loaders():
    """학습용·평가용 DataLoader 를 만든다."""
    ... = datasets.CIFAR10(root='data', 
                     train=True, 
                     transform=transforms.ToTensor(),
                     download=True)


def train_one_epoch(model, loader, criterion, optimizer):
    """한 epoch 학습하고 평균 손실을 반환한다.

    다섯 단계를 순서대로 채우세요.
      1) loader 에서 (x, y) 를 꺼낸다
      2) pred = model(x)
      3) loss = criterion(pred, y)
      4) optimizer.zero_grad() 후 loss.backward()
      5) optimizer.step()

    zero_grad() 를 빠뜨리면 기울기가 누적되어 학습이 망가집니다.
    """
    # TODO: 위 다섯 단계로 학습 루프를 작성하고 평균 손실을 반환하세요.
    raise NotImplementedError


def accuracy(model, loader):
    """테스트셋 정확도를 0~1 사이 실수로 반환한다."""
    raise NotImplementedError

def main():
    torch.manual_seed(42)
    train_loader, test_loader = ...
    model = resnet101(num_classes=NUM_CLASSES, pretrained=False)

    optimizer = torch.optim.Adam(model.parameters(), lr=LEARNING_RATE)  

    for epoch in range(NUM_EPOCHS):
        raise NotImplementedError

    # Serialize once, then split the resulting file into 30 MiB parts.
    buffer = io.BytesIO()
    torch.save(model.state_dict(), buffer)
    serialized_model = buffer.getvalue()
    part_size = 30 * 1024 * 1024

    for part_index, start in enumerate(range(0, len(serialized_model), part_size)):
        with open(f'model_resnet101.pt.part{part_index:03d}', 'wb') as part_file:
            part_file.write(serialized_model[start:start + part_size])
    

if __name__ == "__main__":
    main()
