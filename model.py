# ============================================================
# 2주차 — 모델 정의
#
# submission02.py(학습)와 submission03.py(추론)가 함께 사용합니다.
# 두 곳이 같은 구조를 써야 저장한 가중치를 그대로 불러올 수 있습니다.
# ============================================================
import torch.nn as nn


class MnistNet(nn.Module):
    """28x28 흑백 이미지를 받아 숫자 10개 중 하나로 분류하는 모델."""

    def __init__(self):
        super().__init__()
        # TODO: 아래 세 가지를 만드세요.
        #   self.fc1  : 784 -> 128 인 nn.Linear
        #   self.relu : nn.ReLU
        #   self.fc2  : 128 -> 10 인 nn.Linear
        raise NotImplementedError

    def forward(self, x):
        # TODO: (N, 1, 28, 28) 입력을 (N, 784) 로 편 뒤
        #       fc1 -> relu -> fc2 순서로 통과시켜 반환하세요.
        #       펴는 것은 x.view(x.size(0), -1) 로 할 수 있습니다.
        raise NotImplementedError
