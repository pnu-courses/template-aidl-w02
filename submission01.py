# ============================================================
# 2주차 · 1단계 (과정)  — MNIST 내려받기
#
# 이 파일은 채점되지 않습니다. 최종 제출물인 submission03.py 를
# 만들기 위한 준비 단계이며, 여기서 만든 load_mnist 를
# submission02.py 와 submission03.py 가 그대로 가져다 씁니다.
#
#   $ python3 submission01.py
#   60000
#   10000
#   1 28 28
#   5 0 4 1 9
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
