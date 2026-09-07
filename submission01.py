# ============================================================
# 2주차 · 1단계  — MNIST 표본 10장 만들어 올리기
#
# 개인 PC에서 한 번만 실행하면 됩니다.
#   $ python3 submission01.py
#   saved samples.npz (10 images)
#
# 만들어진 samples.npz 를 저장소에 커밋해 제출하세요.
# 채점기는 이 파일을 실행하지 않고, 여러분이 올린 samples.npz 만 씁니다.
#
# 점검:  $ python3 guideline01.py
# ============================================================
import numpy as np
from torchvision import datasets

DATA_ROOT = "data"
N_SAMPLES = 10
OUT = "samples.npz"


def fetch_samples(n=N_SAMPLES):
    """MNIST 테스트셋 앞 n 장의 이미지와 레이블을 반환한다.

    datasets.MNIST 를 root=DATA_ROOT, train=False, download=True 로 만드세요.
    transform 은 주지 마세요. 그러면 각 원소가 (PIL 이미지, 레이블) 로 나옵니다.

    반환:
      images (n, 28, 28) uint8 배열,  labels (n,) uint8 배열
      PIL 이미지는 np.array(img, dtype=np.uint8) 로 바꿀 수 있습니다.
      순서를 섞지 마세요. 앞에서부터 n 장을 그대로 씁니다.
    """
    # TODO: 위 설명대로 구현하세요.
    raise NotImplementedError


def main():
    images, labels = fetch_samples()
    np.savez_compressed(OUT, images=images, labels=labels)
    print(f"saved {OUT} ({len(images)} images)")


if __name__ == "__main__":
    main()
