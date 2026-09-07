# 2주차 과제 — PyTorch 모델 학습부터 추론 코드 제출까지

> **Ch 1. 개발 환경 구축** · 배점 20점 · 마감 2026-09-14 23:59

## 학습 목표

PyTorch 로 모델을 직접 만들어 학습시키고, 가중치를 .pt 파일로 저장한 뒤, 채점기가 실행할 수 있는 추론 코드까지 제출하는 전 과정을 익힙니다.

## 다루는 개념

- nn.Module 을 상속해 모델을 정의하는 방법 (__init__ 과 forward)
- 학습 루프의 다섯 단계: 데이터 → forward → loss → backward → step
- state_dict 만 저장하는 이유와 model.eval() 의 역할
- Git LFS 로 큰 가중치 파일을 제출하는 방법
- 표준입출력 규약에 맞춘 추론 코드 작성

## 저장소 구성

| 파일 | 역할 |
|---|---|
| `model.py` | 모델 클래스 정의 — `__init__` 과 `forward` 를 채운다 |
| `train.py` | 학습 루프를 돌려 `model.pt` 를 만든다 |
| `inference.py` | `model.pt` 를 불러와 예측을 출력한다 (채점 진입점) |
| `model.pt` | 학습으로 생성되는 가중치 파일 — Git LFS 로 제출 |
| `.gitattributes` | `*.pt` 를 LFS 로 추적하도록 설정 (이미 포함됨) |

## 구현할 내용

각 파일의 `TODO` 를 채우세요. 함수 시그니처와 `inference.py` 의 출력 형식은 바꾸지 마세요.

1. `model.py` — 입력 1개, 출력 1개인 선형 계층을 만들고 forward 를 구현
2. `train.py` — 다섯 단계 학습 루프를 완성하고 state_dict 를 `model.pt` 로 저장
3. `inference.py` — `model.pt` 를 불러오고 eval 모드로 전환해 예측값 출력
4. 학습된 `model.pt` 를 Git LFS 로 커밋해 함께 제출

## 입출력 형식

**입력**

```
inference.py — 한 줄에 실수 x 하나
train.py — 입력 없음
```

**출력**

```
inference.py — 예측값을 반올림한 정수 한 줄
train.py — 마지막 줄에 SAVED
```

## 예시

입력

```
5
```

출력

```
11
```

## 제출 방법

1. 위 파일들의 `TODO` 를 모두 채웁니다.
2. `python3 train.py` 를 실행해 `model.pt` 를 만듭니다.
3. `echo 5 | python3 inference.py` 로 11 이 나오는지 확인합니다.
4. `git lfs install` 후 `git lfs track "*.pt"` 로 가중치를 LFS 로 추적합니다. (`.gitattributes` 는 이미 포함되어 있습니다)
5. `git add . && git commit -m "solve" && git push` — **push 가 곧 제출입니다.**
6. 저장소의 **Actions** 탭에서 자동 채점 결과를 확인합니다.
7. 마감 전까지 몇 번이든 다시 제출할 수 있으며, 마지막 제출이 평가됩니다.

## 평가 기준

| 항목 | 배점 |
|---|---|
| 추론 x=5 | 8 |
| 추론 x=10 | 7 |
| 학습 스크립트 동작 | 5 |
| **합계** | **20** |

---

인공지능융합설계및실험 · 2026-fall · 담당 권용인
