# ============================================================
# 2주차 — 학습 스크립트
#
# 실행하면 model.pt 파일이 만들어집니다.
#   $ python3 train.py
# ============================================================
import torch
import torch.nn as nn

from model import LinearModel

SEED = 0
EPOCHS = 400
LR = 0.05


def make_data():
    """y = 2x + 1 을 따르는 학습 데이터를 만든다.

    x 는 -5 부터 5 까지 21개 점, y 는 정확히 2x + 1 로 둡니다.
    반환: (x, y) 두 개의 (21, 1) 모양 텐서
    """
    # TODO: torch.linspace 로 x 를 만들고 reshape(-1, 1) 하세요. y 는 2*x + 1 입니다.
    raise NotImplementedError


def train():
    """학습 루프를 돌려 학습된 모델을 반환한다.

    다섯 단계를 순서대로 채우세요.
      ① 데이터 준비      ② forward      ③ loss 계산
      ④ backward        ⑤ optimizer.step()
    optimizer.zero_grad() 를 빠뜨리면 기울기가 누적되어 학습이 망가집니다.
    """
    torch.manual_seed(SEED)
    model = LinearModel()
    criterion = nn.MSELoss()
    optimizer = torch.optim.SGD(model.parameters(), lr=LR)

    # TODO: make_data() 로 데이터를 만들고 EPOCHS 만큼 학습 루프를 돌리세요.
    raise NotImplementedError


if __name__ == "__main__":
    m = train()
    torch.save(m.state_dict(), "model.pt")
    print("SAVED model.pt")
