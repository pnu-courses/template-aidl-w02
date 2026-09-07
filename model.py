# ============================================================
# 2주차 — 모델 정의
#
# 학습 대상: y = 2x + 1 인 관계를 선형 계층 하나로 배웁니다.
# ============================================================
import torch.nn as nn


class LinearModel(nn.Module):
    """입력 1개를 받아 출력 1개를 내는 가장 단순한 모델."""

    def __init__(self):
        super().__init__()
        # TODO: 입력 1, 출력 1 인 nn.Linear 계층을 self.fc 로 만드세요.
        raise NotImplementedError

    def forward(self, x):
        # TODO: x 를 self.fc 에 통과시킨 결과를 반환하세요.
        raise NotImplementedError
