# ============================================================
# 2주차 · 최종 제출물  — 올린 결과물로 평가하기
#
# ★ 채점기가 실행하는 파일은 이것 하나입니다. ★
#
# 학습도, 다운로드도 하지 않습니다.
# 여러분이 저장소에 올린 두 파일만 사용합니다.
#   · samples.npz  (1단계 산출물, 약 3KB)
#   · model.pt     (2단계 산출물)
#
#   $ echo "0 1 2" | python3 submission02.py
#   7 2 1
# ============================================================
import sys

import numpy as np
import torch

from model import MnistNet


def load_samples(path="samples.npz"):
    """올려 둔 표본을 모델이 받을 수 있는 텐서로 만든다.

    저장된 images 는 (N, 28, 28) 모양의 0~255 정수입니다.
    다음 순서로 변환하세요.
      1) 255.0 으로 나눠 0~1 범위로 만든다
      2) float32 텐서로 바꾼다
      3) 채널 차원을 넣어 (N, 1, 28, 28) 로 만든다
    """
    # TODO: np.load(path)["images"] 를 위 설명대로 변환해 반환하세요.
    with np.load(path) as data:
        images = data["images"].astype(np.float32) / 255.0
    
    return torch.from_numpy(images).unsqueeze(1)
    


def load_model(path="model.pt"):
    """저장된 가중치를 불러와 추론 준비가 된 모델을 반환한다.

    순서:
      1) MnistNet() 으로 빈 모델을 만든다
      2) torch.load(path) 로 state_dict 를 읽어 load_state_dict 로 넣는다
      3) model.eval() 을 호출해 추론 모드로 바꾼다

    eval() 을 빠뜨리면 Dropout·BatchNorm 이 학습 모드로 남아 결과가 달라집니다.
    """
    # TODO: 위 세 단계를 구현하세요.
    return ...


def predict(model, images, indices):
    """주어진 인덱스들의 예측 숫자를 리스트로 반환한다.

    images 는 (N, 1, 28, 28) 텐서입니다.
    예측은 출력이 가장 큰 인덱스이며, torch.no_grad() 안에서 계산하세요.
    """
    with torch.no_grad():
        outputs = model(images)
        _, predicted = torch.max(outputs, 1)
        return [predicted[i].item() for i in indices]
    



def main():
    indices = [int(v) for v in sys.stdin.read().split()]
    images = load_samples()
    model = load_model()
    print(" ".join(str(v) for v in predict(model, images, indices)))


if __name__ == "__main__":
    main()
