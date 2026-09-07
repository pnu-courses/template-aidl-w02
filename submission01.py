# ============================================================
# 2주차 · 1단계 제출 파일  — MNIST 불러오기
#
# 여기서 만든 load_mnist 를 submission02.py 와 submission03.py 가
# 그대로 가져다 씁니다. 이 함수가 비어 있으면 뒤 단계가 전부 막힙니다.
#
# 완성한 뒤 점검:  $ python3 guideline01.py
# ============================================================
from torchvision import datasets, transforms

DATA_ROOT = "data"


def load_mnist(train):
    """MNIST 데이터셋을 내려받아 Dataset 객체를 반환한다.

    datasets.MNIST 에 다음을 넘기세요.
      root=DATA_ROOT, train=train, download=True,
      transform=transforms.ToTensor()

    ToTensor() 는 0~255 정수 이미지를 0~1 실수 텐서 (1, 28, 28) 로 바꿉니다.
    download=True 이면 data/ 폴더에 없을 때만 내려받습니다.
    """
    # TODO: 위 설명대로 datasets.MNIST 를 만들어 반환하세요.
    raise NotImplementedError
