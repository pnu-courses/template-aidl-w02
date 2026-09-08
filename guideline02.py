# ============================================================
# 2주차 · 2단계  — 개인 PC에서 학습해 model.pt 만들기
#
# 학습은 자원을 많이 쓰므로 채점기에서 돌리지 않습니다.
# 여기서 만든 model.pt 를 저장소에 커밋해 제출하면,
# 채점기는 submission02.py 로 평가만 수행합니다.
#
#   $ python3 guideline02.py
#   epoch 1  loss 0.xxxx
#   test accuracy 0.9xxx
#   saved model.pt
# ============================================================
import torch
import torch.nn as nn
from torch.utils.data import DataLoader
from torchvision import datasets, transforms

from model import MnistNet

DATA_ROOT = "data"
SEED = 0
EPOCHS = 100
BATCH = 128
LR = 1e-3


def loaders():
    """학습용·평가용 DataLoader 를 만든다."""
    tf = transforms.ToTensor()
    train = datasets.MNIST(DATA_ROOT, train=True, download=True, transform=tf)
    test = datasets.MNIST(DATA_ROOT, train=False, download=True, transform=tf)
    return (DataLoader(train, batch_size=BATCH, shuffle=True),
            DataLoader(test, batch_size=512))


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
    torch.manual_seed(SEED)
    train_loader, test_loader = loaders()

    model = MnistNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    for epoch in range(1, EPOCHS + 1):
        loss = train_one_epoch(model, train_loader, criterion, optimizer)
        print(f"epoch {epoch}  loss {loss:.4f}")
        acc = accuracy(model, test_loader)
        print(f"test accuracy {acc:.4f}")
        
    print(f"final test accuracy {acc:.4f}")

    torch.save(model.state_dict(), "model.pt")
    print("saved model.pt")


if __name__ == "__main__":
    main()
