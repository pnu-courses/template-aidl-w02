# ============================================================
# 2주차 제출 03 — 추론  (채점기가 실행하는 파일)
#
# 표준입력으로 MNIST 테스트셋 인덱스들을 받아, 각 이미지의 예측 숫자를
# 공백으로 구분해 한 줄로 출력합니다.
#
#   $ echo "0 1 2" | python3 submission03.py
#   7 2 1
#
# 실행 전에 submission02.py 로 model.pt 를 먼저 만들어야 합니다.
# ============================================================
import sys

import torch

from model import MnistNet
from submission01 import load_mnist


def load_model(path="model.pt"):
    """저장된 가중치를 불러와 추론 준비가 된 모델을 반환한다.

    순서:
      1) MnistNet() 으로 빈 모델을 만든다
      2) torch.load(path) 로 state_dict 를 읽어 load_state_dict 로 넣는다
      3) model.eval() 을 호출해 추론 모드로 바꾼다
    """
    # TODO: 위 세 단계를 구현하세요.
    raise NotImplementedError


def predict(model, dataset, indices):
    """주어진 인덱스들의 예측 숫자를 리스트로 반환한다.

    dataset[i] 는 (이미지 텐서, 정답 레이블) 을 돌려줍니다.
    이미지 하나를 넣을 때는 unsqueeze(0) 으로 배치 차원을 붙이세요.
    torch.no_grad() 안에서 계산하면 더 빠릅니다.
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
