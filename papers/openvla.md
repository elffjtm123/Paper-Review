---
id: openvla
short: "OpenVLA"
title: "OpenVLA: An Open-Source Vision-Language-Action Model"
year: 2024
venue: "Stanford / Berkeley / CoRL 2024"
category: "VLA"
tags: ["Open-Source VLA", "DINOv2", "SigLIP", "LLaMA", "LoRA"]
pdf: "논문/VLA/OpenVLA.pdf"
predecessors: ["rt-2", "rt-x", "llama", "dinov2", "siglip", "lora"]
successors: ["openvla-oft", "pi-0", "fast", "wall-oss"]
---

## 한 줄 요약
DINOv2 + SigLIP 이중 비전 인코더와 Llama 2 7B를 결합해 OXE 97만 궤적으로 학습한 대표 오픈소스 7B VLA 모델.

## 핵심 메커니즘
- 공간 기하에 강한 DINOv2와 의미 이해에 강한 SigLIP 특징을 채널 결합(Prismatic VLM 기반).
- 연속 7D 액션을 256구간(1~99% 분위수) 이산 토큰으로 매핑해 Llama 2의 하위 사용 빈도 토큰 256개로 대체.
- LoRA·4bit 양자화 미세조정을 지원해 소비자 GPU에서도 새 작업 적응 가능.

## 기존 대비 차이
55B 폐쇄형 RT-2-X보다 7배 이상 작으면서도 다중 작업에서 성능을 앞서고, 모델·코드·학습 파이프라인을 전면 공개.

## 한계 & 연결
단일 스텝 자기회귀 이산 토큰 방식이라 추론 속도가 느리고(약 6Hz) 양팔·고주파 정밀 제어에 취약 → **OpenVLA-OFT**, **FAST**, **π0**로 발전.
