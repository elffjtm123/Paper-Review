---
id: siglip
short: "SigLIP"
title: "Sigmoid Loss for Language Image Pre-Training"
year: 2023
venue: "Zhai et al. (Google) / ICCV 2023"
category: "Multimodal"
tags: ["Sigmoid Loss", "VLM Encoder", "Small Batch", "Contrastive"]
pdf: "논문/Multimodal/SigLIP.pdf"
predecessors: ["clip", "vit"]
successors: ["openvla", "pi-0"]
---

## 한 줄 요약
CLIP의 전역 Softmax 대조손실을 이미지-텍스트 쌍별 독립 Sigmoid 이진 분류 손실로 바꿔, 작은 배치와 분산 학습 효율을 크게 높인 비전-언어 인코더.

## 핵심 메커니즘
- 배치 전체 유사도를 정규화하는 Softmax 대신, 각 (이미지, 텍스트) 쌍을 독립적인 이진 로지스틱 손실로 계산.
- 전역 정규화가 없어 디바이스 간 통신(All-Gather) 비용이 줄고, 작은/중간 배치에서도 고성능 + 초거대 배치 확장 용이.
- 불균형(음성 쌍 압도)을 학습 가능한 초기 음수 bias로 안정화.

## 기존 대비 차이
CLIP보다 구현·분산 학습이 훨씬 가볍고 고해상도/소배치 효율이 뛰어나 PaliGemma·π0·OpenVLA 등 최신 VLM/VLA의 사실상 표준 비전 인코더가 됨.

## 한계 & 연결
순수 이미지-텍스트 정렬 인코더라 정밀 3D/밀집 기하 정보는 DINOv2 등에 비해 상대적으로 부족할 수 있음.
