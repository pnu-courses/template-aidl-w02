# ============================================================
# 2주차 — 추론 진입점  (채점기가 실행하는 파일)
#
# 표준입력으로 실수 x 하나를 받아, 예측값을 반올림한 정수를 출력합니다.
#   $ echo 5 | python3 inference.py
#   11
#
# 실행 전에 train.py 로 model.pt 를 먼저 만들어야 합니다.
# ============================================================
import sys

import torch

from model import LinearModel


def load_model(path="model.pt"):
    """저장된 가중치를 불러와 추론 준비가 된 모델을 반환한다.

    순서:
      1) LinearModel() 로 빈 모델을 만든다
      2) torch.load(path) 로 state_dict 를 읽어 load_state_dict 로 넣는다
      3) model.eval() 을 호출해 추론 모드로 바꾼다
    """
    # TODO: 위 세 단계를 구현하세요.
    raise NotImplementedError


def predict(model, x):
    """x 하나에 대한 예측값을 파이썬 실수로 반환한다.

    torch.no_grad() 안에서 계산하면 기울기를 만들지 않아 더 빠릅니다.
    """
    # TODO: x 를 (1, 1) 모양 텐서로 만들어 모델에 넣고, 결과를 float 로 꺼내세요.
    raise NotImplementedError


def main():
    x = float(sys.stdin.read().split()[0])
    model = load_model()
    y = predict(model, x)
    print(int(round(y)))


if __name__ == "__main__":
    main()
