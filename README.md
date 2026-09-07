# 2주차 과제 — MNIST 내려받아 학습하고 추론 코드 제출하기

> **Ch 1. 개발 환경 구축** · 배점 20점 · 마감 2026-09-14 23:59

## 학습 목표

MNIST 데이터셋을 내려받아 PyTorch 모델을 직접 학습시키고, 가중치를 .pt 파일로 저장한 뒤, 채점기가 실행할 수 있는 추론 코드까지 제출하는 전 과정을 익힙니다.

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
| `submission01.py` | MNIST 를 내려받고 데이터 통계를 출력한다 |
| `submission02.py` | 모델을 학습시켜 `model.pt` 를 만들고 정확도를 출력한다 |
| `submission03.py` | `model.pt` 를 불러와 주어진 인덱스의 숫자를 예측한다 |
| `model.py` | 세 제출 파일이 함께 쓰는 모델 클래스 정의 |
| `model.pt` | 학습으로 생성되는 가중치 파일 — Git LFS 로 제출 |
| `.gitattributes` | `*.pt` 를 LFS 로 추적하도록 설정 (이미 포함됨) |

## 구현할 내용

각 파일의 `TODO` 를 채우세요. 함수 시그니처와 `submission01.py` 의 출력 형식은 바꾸지 마세요.

1. `model.py` — 784 → 128 → 10 인 분류 모델을 정의
2. `submission01.py` — MNIST 를 내려받아 학습/검증 표본 수와 이미지 모양을 출력
3. `submission02.py` — 학습 루프를 완성하고 `model.pt` 저장, 테스트 정확도 출력
4. `submission03.py` — `model.pt` 를 불러와 표준입력으로 받은 인덱스들의 예측을 출력
5. 학습된 `model.pt` 를 Git LFS 로 커밋해 함께 제출

## 입출력 형식

**입력**

```
submission01.py, submission02.py — 입력 없음
submission03.py — 한 줄에 MNIST 테스트셋 인덱스들 (공백 구분)
```

**출력**

```
submission01.py — 학습 표본 수 / 검증 표본 수 / 이미지 모양 / 앞 5개 레이블
submission02.py — 마지막 줄에 PASS (정확도 90% 이상) 또는 FAIL
submission03.py — 예측한 숫자들을 공백으로 구분해 한 줄
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
2. `python3 submission01.py` 로 MNIST 가 정상적으로 내려받아지는지 확인합니다.
3. `python3 submission02.py` 를 실행해 `model.pt` 를 만들고 PASS 가 나오는지 확인합니다.
4. `echo "0 1 2" | python3 submission03.py` 로 `7 2 1` 이 나오는지 확인합니다.
5. `git lfs install` 후 `git lfs track "*.pt"` 로 가중치를 LFS 로 추적합니다. (`.gitattributes` 는 이미 포함되어 있습니다)
6. `git add . && git commit -m "solve" && git push` — **push 가 곧 제출입니다.**
7. 저장소의 **Actions** 탭에서 자동 채점 결과를 확인합니다.
8. 마감 전까지 몇 번이든 다시 제출할 수 있으며, 마지막 제출이 평가됩니다.

## 평가 기준

| 항목 | 배점 |
|---|---|
| MNIST 내려받기 | 6 |
| 학습 정확도 90% 이상 | 7 |
| 추론 결과 | 7 |
| **합계** | **20** |

---

인공지능융합설계및실험 · 2026-fall · 담당 권용인
