# ============================================================
# 2주차 — 모델 정의
#
# guideline02.py(학습)와 submission02.py(평가)가 함께 사용합니다.
# 두 곳이 같은 구조를 써야 저장한 가중치를 그대로 불러올 수 있습니다.
# ============================================================
import torch.nn as nn


class MnistNet(nn.Module):
    """28x28 흑백 이미지를 받아 숫자 10개 중 하나로 분류하는 모델."""

    # def __init__(self):
    #     super().__init__()
    #     # TODO: 아래 세 가지를 만드세요.
    #     #   self.fc1  : 784 -> 128 인 nn.Linear
    #     #   self.relu : nn.ReLU
    #     #   self.fc2  : 128 -> 10 인 nn.Linear
    #     raise NotImplementedError

    # def forward(self, x):
    #     # TODO: (N, 1, 28, 28) 입력을 (N, 784) 로 편 뒤
    #     #       fc1 -> relu -> fc2 순서로 통과시켜 반환하세요.
    #     #       펴는 것은 x.view(x.size(0), -1) 로 할 수 있습니다.
    #     raise NotImplementedError

    def __init__(self):
        super(MnistNet, self).__init__()
        self.conv1 = nn.Conv2d(1, 6, 5)
        self.relu1 = nn.ReLU()
        self.pool1 = nn.MaxPool2d(2)
        self.conv2 = nn.Conv2d(6, 16, 5)
        self.relu2 = nn.ReLU()
        self.pool2 = nn.MaxPool2d(2)
        self.fc1 = nn.Linear(256, 120)
        self.relu3 = nn.ReLU()
        self.fc2 = nn.Linear(120, 84)
        self.relu4 = nn.ReLU()
        self.fc3 = nn.Linear(84, 10)
        self.relu5 = nn.ReLU()

    def forward(self, x):
        y = self.conv1(x)
        y = self.relu1(y)
        y = self.pool1(y)
        y = self.conv2(y)
        y = self.relu2(y)
        y = self.pool2(y)
        y = y.view(y.shape[0], -1)
        y = self.fc1(y)
        y = self.relu3(y)
        y = self.fc2(y)
        y = self.relu4(y)
        y = self.fc3(y)
        y = self.relu5(y)
        return y