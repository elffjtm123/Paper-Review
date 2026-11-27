---
id: dinov2
short: "DINOv2"
title: "DINOv2: Learning Robust Visual Features without Supervision"
year: 2023
venue: "Oquab et al. (Meta) / TMLR 2024"
category: "Multimodal"
tags: ["Visual Foundation", "Data Curation", "iBOT", "Dense Features"]
pdf: "논문/Multimodal/DINOv2.pdf"
predecessors: ["dino", "vit"]
successors: ["openvla"]
---

## 한 줄 요약
자동 데이터 큐레이션 파이프라인(LVD-142M)과 DINO+iBOT(패치 마스킹) 결합으로 깊이 추정·분할·로봇 조작 등 밀집 시각 과제에 최강인 범용 비전 백본.

## 핵심 메커니즘
- 중복 제거 + 대표 데이터 기반 검색으로 정제한 1.42억 장 큐레이션 데이터셋(LVD-142M) 구축.
- 이미지 수준 자기증류(DINO) + 패치 수준 마스크 복원(iBOT) + KoLeo 정규화로 전역·지역 특징을 동시에 강화.
- 대형 ViT-g(1.1B)를 학습한 뒤 소형 모델로 증류(distillation)해 고효율 백본 제공.

## 기존 대비 차이
언어 정렬 모델(CLIP/SigLIP)이 약한 기하·깊이·공간 위치 같은 밀집(dense) 시각 특징에 압도적이라, OpenVLA가 SigLIP과 함께 이중 비전 인코더로 채택.

## 한계 & 연결
언어 의미 정렬이 없으므로 VLM/VLA에서는 텍스트 정렬 인코더(SigLIP 등)와 결합하거나 별도 프로젝션이 필요.
