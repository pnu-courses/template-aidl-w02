# 2주차 과제 — 환경 세팅과 PyTorch 모델 학습·제출


## 학습 목표

무거운 작업은 개인 PC에서 합니다. 학습은 각자 PC에서 돌려 **산출물(표본·가중치)** 을 저장소에 올리고,
채점기는 올라온 산출물로 **추론만** 수행합니다.

## 다루는 개념

- PyTorch 텐서와 NumPy 배열의 관계 (`.numpy()`, `torch.from_numpy`, `torch.allclose`)
- `nn.Module` 을 상속해 모델을 정의하는 방법 (`__init__` 과 `forward`)
- 학습 루프의 다섯 단계: 데이터 → forward → loss → backward → step
- `state_dict` 만 저장하는 이유와 `model.eval()` 의 역할
- torchvision 으로 표준 데이터셋(MNIST · CIFAR-10)을 내려받는 방법
- 학습 산출물과 실행 코드를 분리해 관리하는 이유
- uv 로 잠긴 의존성을 재현해 채점기와 같은 환경을 만드는 방법

## 이번 주 과제

| # | 내용 | 관련 파일 |
|---|---|---|
| 1 | PyTorch 와 NumPy 로 1024 × 1024 행렬 곱셈을 구현하고 결과가 일치하는지 확인한다 | `submission01.py` |
| 2 | LeNet-5 를 MNIST 로 학습해 가중치를 만들고, 그 가중치로 추론 결과를 출력한다 | `model.py` · `guideline02.py` · `submission02.py` |
| 3 | ResNet-101 을 CIFAR-10 으로 학습해 가중치를 제출한다 | `guideline03.py` · `submission03.py` |

## 과제 1 — 행렬 곱셈

`submission01.py` 의 `torch_matmul` 과 `numpy_matmul` 을 구현합니다.
1024 × 1024 무작위 행렬 두 개를 곱한 뒤, 두 결과가 `torch.allclose` 로 일치하는지 확인합니다.

```bash
uv run submission01.py
```

## 과제 2 — LeNet-5 · MNIST

**입력** — `submission02.py` 은 한 줄에 표본 인덱스들(0~9, 공백 구분)을 받습니다.
**출력** — 예측한 숫자들을 공백으로 구분해 한 줄로 출력합니다.

```
입력    0 1 2
출력    7 2 1
```

```bash
uv run guideline02.py                   # 개인 PC에서 학습 → model.pt 생성
echo "0 1 2" | uv run submission02.py   # 7 2 1 이 나오는지 확인 (채점 대상)
```

`guideline02.py` 는 개인 PC용이며 채점하지 않습니다. 채점기가 실행하는 파일은 `submission02.py` 하나입니다.

## 과제 3 — ResNet-101 · CIFAR-10

`guideline03.py` 로 ResNet-101 을 CIFAR-10 으로 학습하고, `submission03.py` 로 추론합니다.

```bash
uv run guideline02.py                   # 개인 PC에서 학습 → 분할 압축된 model.pt 생성
echo "0 1 2" | uv run submission03.py   # 7 2 1 이 나오는지 확인 (채점 대상)
```
