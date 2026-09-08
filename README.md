# 2주차 과제 — 학습된 모델 평가 및 제출 방법 설명 가이드라인

> **Ch 1. 개발 환경 구축** · 배점 20점 · 마감 2026-09-14 23:59

## 학습 목표

무거운 작업은 개인 PC에서 합니다. MNIST 표본 10장을 직접 뽑아 올리고, 모델을 학습해 가중치를 올린 뒤, 채점기에서는 올린 결과물로 평가만 수행합니다.

## 다루는 개념

- torchvision 으로 표준 데이터셋을 내려받는 방법
- 학습 산출물(데이터·가중치)과 실행 코드를 분리해 관리하는 이유
- nn.Module 을 상속해 모델을 정의하는 방법 (__init__ 과 forward)
- 학습 루프의 다섯 단계: 데이터 → forward → loss → backward → step
- state_dict 만 저장하는 이유와 model.eval() 의 역할
- uv 로 잠긴 의존성을 재현해 채점기와 같은 환경을 만드는 방법

## 저장소 구성

| 파일 | 역할 |
|---|---|
| `submission01.py` | **1단계** MNIST 테스트셋 앞 10장을 뽑아 `samples.npz` 로 저장한다 |
| `guideline01.py` | └ 개인 PC 점검 — 만들어진 `samples.npz` 가 올바른지 확인해 준다 |
| `guideline02.py` | **2단계** 개인 PC에서 모델을 학습해 `model.pt` 를 만든다 |
| `submission02.py` | **최종 제출물** — 올린 `samples.npz` 와 `model.pt` 로 평가만 수행 (채점 대상) |
| `model.py` | 학습과 평가가 함께 쓰는 모델 클래스 정의 |
| `samples.npz` | 1단계 산출물 — 저장소에 커밋해 제출 |
| `model.pt` | 2단계 산출물 — 저장소에 커밋해 제출 |
| `pyproject.toml` | 의존성 정의 — `uv sync` 가 이 파일을 읽는다 |
| `uv.lock` | 잠긴 의존성 버전 — 채점기와 같은 환경을 재현한다 (수정하지 마세요) |
| `.python-version` | 이 과제가 쓰는 파이썬 버전 (3.12) |

## 구현할 내용

각 파일의 `TODO` 를 채우세요. 함수 시그니처와 `submission02.py` 의 출력 형식은 바꾸지 마세요.

1. `model.py` — 784 → 128 → 10 인 분류 모델을 정의한다
2. `submission01.py` — MNIST 테스트셋 앞 10장을 `samples.npz` 로 저장한다 (개인 PC)
3. `guideline02.py` — 학습 루프를 완성해 `model.pt` 를 만든다 (개인 PC)
4. `submission02.py` — 올린 `samples.npz` 와 `model.pt` 로 예측을 출력한다 (채점 대상)
5. `samples.npz` 와 `model.pt` 를 저장소에 커밋해 함께 제출한다

## 입출력 형식

**입력**

```
submission02.py — 한 줄에 표본 인덱스들 (0~9, 공백 구분)
```

**출력**

```
submission02.py — 예측한 숫자들을 공백으로 구분해 한 줄

(submission01.py 와 guideline01/02.py 는 개인 PC용이며 채점하지 않습니다)
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
2. 개인 PC에 [uv](https://docs.astral.sh/uv/) 를 설치한 뒤 `uv sync` 로 작업 환경을 준비합니다. `uv.lock` 에 잠긴 그대로 설치되므로 채점기와 같은 환경이 됩니다.
3. `uv run submission01.py` 를 실행해 `samples.npz` 를 만들고, `uv run guideline01.py` 로 점검합니다.
4. `uv run guideline02.py` 를 실행해 학습하고 `model.pt` 를 만듭니다.
5. `echo "0 1 2" | uv run submission02.py` 로 `7 2 1` 이 나오는지 확인합니다. **채점되는 것은 이 파일입니다.**
6. `git add . && git commit -m "solve" && git push` — **push 가 곧 제출입니다.**
7. 저장소의 **Actions** 탭에서 자동 채점 결과를 확인합니다.
8. 마감 전까지 몇 번이든 다시 제출할 수 있으며, 마지막 제출이 평가됩니다.

`.gitignore` 가 `*.pt` 를 무시하지만 바로 아래 `!model.pt` 예외가 있어 `model.pt` 는 그대로 커밋됩니다. `git add` 후 `git status` 에 `samples.npz` 와 `model.pt` 가 올라왔는지 꼭 확인하세요. 두 파일이 없으면 채점기가 평가할 대상이 없습니다.

## 평가 기준

| 항목 | 배점 |
|---|---|
| 평가 — 한 개 | 4 |
| 평가 — 세 개 | 6 |
| 평가 — 다섯 개 | 10 |
| **합계** | **20** |

---

인공지능융합설계및실험 · 2026-fall · 담당 권용인
