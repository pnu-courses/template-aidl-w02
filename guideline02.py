# ============================================================
# 2주차 · 2단계 점검  — model.pt 가 쓸 만한지 확인
#
# 이 파일은 고치지 않아도 됩니다. submission02.py 로 학습을 끝낸 뒤
# 그냥 실행만 하세요.
#   $ python3 guideline02.py
#
# 학생 코드의 정확도 계산을 믿지 않고, 여기서 직접 다시 잽니다.
# ============================================================
import os

import torch
from torch.utils.data import DataLoader

from model import MnistNet
from submission01 import load_mnist

THRESHOLD = 0.90


def accuracy(model, loader):
    """테스트셋 정확도를 직접 계산한다."""
    model.eval()
    correct = total = 0
    with torch.no_grad():
        for x, y in loader:
            pred = model(x).argmax(dim=1)
            correct += int((pred == y).sum())
            total += int(y.numel())
    return correct / total


def main():
    if not os.path.exists("model.pt"):
        print("model.pt 가 없습니다. 먼저 python3 submission02.py 를 실행하세요.")
        return

    model = MnistNet()
    model.load_state_dict(torch.load("model.pt"))
    loader = DataLoader(load_mnist(False), batch_size=512)

    acc = accuracy(model, loader)
    print(f"테스트 정확도: {acc:.4f}   기준 {THRESHOLD:.2f}")
    if acc >= THRESHOLD:
        print("==> 2단계 통과")
    else:
        print("==> 2단계 실패 — 학습 루프를 다시 확인하세요")


if __name__ == "__main__":
    main()
