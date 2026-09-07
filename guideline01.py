# ============================================================
# 2주차 · 1단계 점검  — samples.npz 가 제대로 만들어졌는지 확인
#
# 이 파일은 고치지 않아도 됩니다. 그냥 실행만 하세요.
#   $ python3 guideline01.py
#
# 채점기는 여러분이 올린 samples.npz 를 그대로 믿고 씁니다.
# 여기서 통과하지 못하면 채점도 통과할 수 없습니다.
# ============================================================
import os

import numpy as np

EXPECT_N = 10
EXPECT_SHAPE = (28, 28)
EXPECT_LABELS = [7, 2, 1, 0, 4, 1, 4, 9, 5, 9]


def check(name, got, want):
    ok = got == want
    print(f"{name:<14}: {got}   기대 {want}   {'OK' if ok else '불일치'}")
    return ok


def main():
    if not os.path.exists("samples.npz"):
        print("samples.npz 가 없습니다. 먼저 python3 submission01.py 를 실행하세요.")
        return

    d = np.load("samples.npz")
    images, labels = d["images"], d["labels"]

    results = [
        check("표본 개수", len(images), EXPECT_N),
        check("이미지 모양", tuple(images.shape[1:]), EXPECT_SHAPE),
        check("자료형", str(images.dtype), "uint8"),
        check("레이블", [int(v) for v in labels], EXPECT_LABELS),
    ]
    print("==> 1단계 통과" if all(results)
          else "==> 1단계 실패 — submission01.py 를 다시 확인하세요")


if __name__ == "__main__":
    main()
