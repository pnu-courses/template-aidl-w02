# ============================================================
# 2주차 제출 02 — 학습
#
# 실행하면 MNIST 로 모델을 학습시키고 model.pt 를 만듭니다.
#   $ python3 submission02.py
#
# 마지막 줄에 정확도가 90% 이상이면 PASS, 아니면 FAIL 을 출력합니다.
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
THRESHOLD = 0.90


def train_one_epoch(model, loader, criterion, optimizer):
    """한 epoch 학습한다. 다섯 단계를 순서대로 채우세요.

      ① loader 에서 (x, y) 를 꺼낸다
      ② pred = model(x)
      ③ loss = criterion(pred, y)
      ④ optimizer.zero_grad() 후 loss.backward()
      ⑤ optimizer.step()

    zero_grad() 를 빠뜨리면 기울기가 누적되어 학습이 망가집니다.
    """
    model.train()
    # TODO: 위 다섯 단계로 학습 루프를 작성하세요.
    raise NotImplementedError


def evaluate(model, loader):
    """테스트셋 정확도를 0~1 사이 실수로 반환한다.

    torch.no_grad() 안에서 계산하고, 예측은 출력이 가장 큰 인덱스입니다.
    """
    model.eval()
    # TODO: 맞힌 개수 / 전체 개수 를 반환하세요.
    raise NotImplementedError


def main():
    torch.manual_seed(SEED)
    train_loader = DataLoader(load_mnist(True), batch_size=BATCH, shuffle=True)
    test_loader = DataLoader(load_mnist(False), batch_size=512)

    model = MnistNet()
    criterion = nn.CrossEntropyLoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=LR)

    for _ in range(EPOCHS):
        train_one_epoch(model, train_loader, criterion, optimizer)

    acc = evaluate(model, test_loader)
    torch.save(model.state_dict(), "model.pt")
    print(f"ACC {acc:.4f}")
    print("PASS" if acc >= THRESHOLD else "FAIL")


if __name__ == "__main__":
    main()
