# 2주차 과제 — MNIST 내려받아 학습하고 추론 코드 제출하기

> **Ch 1. 개발 환경 구축** · 배점 20점 · 마감 2026-09-14 23:59

## 학습 목표

MNIST 를 내려받아 모델을 학습시키고, 그 결과물인 추론 코드를 제출합니다. 데이터 준비와 학습은 최종 제출물을 만들기 위한 과정이며, 채점은 submission03.py 하나로 이루어집니다.

## 다루는 개념

- torchvision 으로 표준 데이터셋을 내려받고 DataLoader 로 배치를 만드는 방법
- nn.Module 을 상속해 모델을 정의하는 방법 (__init__ 과 forward)
- 학습 루프의 다섯 단계: 데이터 → forward → loss → backward → step
- state_dict 만 저장하는 이유와 model.eval() 의 역할
- Git LFS 로 큰 가중치 파일을 제출하는 방법
- 표준입출력 규약에 맞춘 추론 코드 작성

## 저장소 구성

| 파일 | 역할 |
|---|---|
| `submission01.py` | **1단계 (과정)** MNIST 를 내려받고 데이터를 확인한다 |
| `submission02.py` | **2단계 (과정)** 모델을 학습시켜 `model.pt` 를 만든다 |
| `submission03.py` | **3단계 · 최종 제출물** — 채점기가 실행하는 유일한 파일 |
| `model.py` | 세 파일이 함께 쓰는 모델 클래스 정의 |
| `model.pt` | 2단계에서 생성되는 가중치 — Git LFS 로 함께 제출 |
| `.gitattributes` | `*.pt` 를 LFS 로 추적하도록 설정 (이미 포함됨) |

## 구현할 내용

각 파일의 `TODO` 를 채우세요. 함수 시그니처와 `submission03.py` 의 출력 형식은 바꾸지 마세요.

1. `model.py` — 784 → 128 → 10 인 분류 모델을 정의한다
2. `submission01.py` (과정) — MNIST 를 내려받는 `load_mnist` 를 완성한다
3. `submission02.py` (과정) — 학습 루프를 완성해 `model.pt` 를 만든다
4. `submission03.py` (최종 제출) — `model.pt` 를 불러와 주어진 인덱스의 숫자를 예측한다
5. 완성된 `model.pt` 를 Git LFS 로 커밋해 함께 제출한다

## 입출력 형식

**입력**

```
submission03.py — 한 줄에 MNIST 테스트셋 인덱스들 (공백 구분)
```

**출력**

```
submission03.py — 예측한 숫자들을 공백으로 구분해 한 줄

(submission01.py 와 submission02.py 는 과정 파일이라 채점하지 않습니다)
```

## 예시

입력

```
0 1 2
```

출력

```
7 2 1
```

## 제출 방법

1. 위 파일들의 `TODO` 를 모두 채웁니다.
2. `python3 submission01.py` 로 MNIST 가 정상적으로 내려받아지는지 확인합니다. (과정 확인용)
3. `python3 submission02.py` 를 실행해 `model.pt` 를 만들고 정확도가 90% 이상인지 확인합니다. (과정 확인용)
4. `echo "0 1 2" | python3 submission03.py` 로 `7 2 1` 이 나오는지 확인합니다. **채점되는 것은 이 파일입니다.**
5. `git lfs install` 후 `git lfs track "*.pt"` 로 가중치를 추적합니다. (`.gitattributes` 는 이미 포함되어 있습니다)
6. `git add . && git commit -m "solve" && git push` — **push 가 곧 제출입니다.**
7. 저장소의 **Actions** 탭에서 자동 채점 결과를 확인합니다.
8. 마감 전까지 몇 번이든 다시 제출할 수 있으며, 마지막 제출이 평가됩니다.

## 평가 기준

| 항목 | 배점 |
|---|---|
| 추론 — 한 개 | 4 |
| 추론 — 세 개 | 6 |
| 추론 — 다섯 개 | 10 |
| **합계** | **20** |

---

인공지능융합설계및실험 · 2026-fall · 담당 권용인
