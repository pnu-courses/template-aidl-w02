# ============================================================
# 2주차 · 3단계 — 최종 제출물
#
# ★ 채점기가 실행하는 파일은 이것 하나입니다. ★
#
# 표준입력으로 MNIST 테스트셋 인덱스들을 받아, 각 이미지의 예측 숫자를
# 공백으로 구분해 한 줄로 출력합니다.
#
#   $ echo "0 1 2" | python3 submission03.py
#   7 2 1
#
# 실행 조건
#   · guideline01.py 의 load_mnist 가 완성되어 있어야 합니다.
#   · guideline02.py 를 먼저 실행해 model.pt 를 만들어 두어야 합니다.
# ============================================================
import sys

import torch

from model import MnistNet
from guideline01 import load_mnist


def load_model(path="model.pt"):
    """저장된 가중치를 불러와 추론 준비가 된 모델을 반환한다.

    순서:
      1) MnistNet() 으로 빈 모델을 만든다
      2) torch.load(path) 로 state_dict 를 읽어 load_state_dict 로 넣는다
      3) model.eval() 을 호출해 추론 모드로 바꾼다

    eval() 을 빠뜨리면 Dropout·BatchNorm 이 학습 모드로 남아 결과가 달라집니다.
    """
    # TODO: 위 세 단계를 구현하세요.
    raise NotImplementedError


def predict(model, dataset, indices):
    """주어진 인덱스들의 예측 숫자를 리스트로 반환한다.

    dataset[i] 는 (이미지 텐서, 정답 레이블) 을 돌려줍니다.
    이미지 하나를 넣을 때는 unsqueeze(0) 으로 배치 차원을 붙이세요.
    예측은 출력이 가장 큰 인덱스이며, torch.no_grad() 안에서 계산하면 더 빠릅니다.
    """
    # TODO: 각 인덱스마다 예측한 숫자를 모아 반환하세요.
    raise NotImplementedError


def main():
    indices = [int(v) for v in sys.stdin.read().split()]
    model = load_model()
    test_set = load_mnist(False)
    print(" ".join(str(v) for v in predict(model, test_set, indices)))


if __name__ == "__main__":
    main()
