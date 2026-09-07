# ============================================================
# 2주차 제출 01 — MNIST 내려받기
#
# 실행하면 MNIST 를 data/ 폴더에 내려받고 통계를 출력합니다.
#   $ python3 submission01.py
#   60000
#   10000
#   1 28 28
#   5 0 4 1 9
#
# 여기서 만든 load_mnist 는 submission02.py, submission03.py 도 함께 씁니다.
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


def main():
    train_set = load_mnist(True)
    test_set = load_mnist(False)

    print(len(train_set))
    print(len(test_set))

    image, _ = train_set[0]
    print(image.shape[0], image.shape[1], image.shape[2])

    print(" ".join(str(int(train_set[i][1])) for i in range(5)))


if __name__ == "__main__":
    main()
