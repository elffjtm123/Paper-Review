---
id: qlora
short: "QLoRA"
title: "QLoRA: Efficient Finetuning of Quantized LLMs"
year: 2023
venue: "Dettmers et al. / NeurIPS 2023"
category: "Optimization"
tags: ["4-bit", "NF4", "Double Quantization", "Paged Optimizers", "PEFT"]
pdf: "논문/Optimization/QLoRA.pdf"
predecessors: ["lora", "llama"]
successors: ["dora"]
---

## 한 줄 요약
동결 베이스 모델을 4-bit NormalFloat(NF4)로 양자화하고 역전파 시에만 BF16으로 복원해 LoRA를 학습, 단일 48GB GPU에서 65B LLM 미세조정을 가능케 한 기법.

## 핵심 메커니즘
- NF4(4-bit NormalFloat): 정규분포 가중치에 정보이론적으로 최적인 비균일 4비트 양자화 포맷.
- Double Quantization: 양자화 상수(scaling factor) 자체를 한 번 더 양자화해 파라미터당 0.37비트 추가 절감.
- Paged Optimizers: NVIDIA 통합 메모리를 활용해 긴 시퀀스 그래디언트 스파이크 시 CPU↔GPU 자동 페이징으로 OOM 방지.

## 기존 대비 차이
LoRA에서 여전히 남았던 베이스 모델 FP16 로딩 메모리 병목을 4비트로 1/4 압축하면서도 16비트 Full FT와 동등한 성능을 유지.

## 한계 & 연결
순전파/역전파마다 4bit→BF16 디양자화 오버헤드가 있어 학습 속도는 순수 FP16 LoRA보다 다소 느림.
