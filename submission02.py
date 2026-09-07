# ============================================================
# 2주차 · 2단계 제출 파일  — 학습해서 model.pt 만들기
#
# 실행하면 MNIST 로 모델을 학습시키고 model.pt 를 저장합니다.
#   $ python3 submission02.py
#
# 완성한 뒤 점검:  $ python3 guideline02.py
# ============================================================
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from model import MnistNet
from submission01 import load_mnist

SEED = 0
EPOCHS = 1
BATCH = 128
LR = 1e-3


def train_one_epoch(model, loader, criterion, optimizer):
    """한 epoch 학습한다. 다섯 단계를 순서대로 채우세요.

      1) loader 에서 (x, y) 를 꺼낸다
      2) pred = model(x)
      3) loss = criterion(pred, y)
      4) optimizer.zero_grad() 후 loss.backward()
      5) optimizer.step()

    zero_grad() 를 빠뜨리면 기울기가 누적되어 학습이 망가집니다.
    """
    model.train()
    # TODO: 위 다섯 단계로 학습 루프를 작성하세요.
    raise NotImplementedError


def main():
    torch.manual_seed(SEED)
    loader = DataLoader(load_mnist(True), batch_size=BATCH, shuffle=True)

    model = MnistNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    for _ in range(EPOCHS):
        train_one_epoch(model, loader, criterion, optimizer)

    torch.save(model.state_dict(), "model.pt")
    print("saved model.pt")


if __name__ == "__main__":
    main()
