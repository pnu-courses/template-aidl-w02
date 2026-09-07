# ============================================================
# 2주차 · 1단계 점검  — submission01.py 가 맞게 됐는지 확인
#
# 이 파일은 고치지 않아도 됩니다. 그냥 실행만 하세요.
#   $ python3 guideline01.py
#
# 통과하면 아래처럼 나옵니다.
#   학습 표본 수 : 60000   기대 60000   OK
#   검증 표본 수 : 10000   기대 10000   OK
#   이미지 모양  : 1 28 28  기대 1 28 28  OK
#   앞 5개 레이블: 5 0 4 1 9  기대 5 0 4 1 9  OK
#   ==> 1단계 통과
# ============================================================
from submission01 import load_mnist

EXPECT_TRAIN = 60000
EXPECT_TEST = 10000
EXPECT_SHAPE = (1, 28, 28)
EXPECT_LABELS = [5, 0, 4, 1, 9]


def check(name, got, want):
    ok = got == want
    print(f"{name:<12}: {got}   기대 {want}   {'OK' if ok else '불일치'}")
    return ok


def main():
    train_set = load_mnist(True)
    test_set = load_mnist(False)
    image, _ = train_set[0]

    results = [
        check("학습 표본 수", len(train_set), EXPECT_TRAIN),
        check("검증 표본 수", len(test_set), EXPECT_TEST),
        check("이미지 모양", tuple(image.shape), EXPECT_SHAPE),
        check("앞 5개 레이블", [int(train_set[i][1]) for i in range(5)], EXPECT_LABELS),
    ]
    print("==> 1단계 통과" if all(results) else "==> 1단계 실패 — submission01.py 를 다시 확인하세요")


if __name__ == "__main__":
    main()
