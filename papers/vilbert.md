---
id: vilbert
short: "ViLBERT"
title: "ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks"
year: 2019
venue: "Lu et al. / NeurIPS 2019"
category: "Multimodal"
tags: ["Two-Stream", "Co-Attention", "VLM Pretraining", "BERT"]
pdf: "논문/Multimodal/ViLBERT.pdf"
predecessors: ["bert", "r-cnn"]
successors: ["clip"]
---

## 한 줄 요약
시각(객체 영역 특징)과 언어 스트림을 분리해 처리하되 Co-Attention 레이어로 상호작용시킨 초기 양방향 비전-언어 사전학습 모델.

## 핵심 메커니즘
- Faster R-CNN으로 추출한 이미지 영역 특징과 텍스트 토큰을 각각 별도 Transformer 스트림으로 인코딩.
- Co-Attention Transformer 블록에서 두 모달리티의 Key/Value를 서로 교환해 교차 참조.
- Masked Multi-Modal Modelling + Multi-Modal Alignment(이미지-캡션 일치 판별) 2가지 사전학습 과제.

## 기존 대비 차이
단일 스트림으로 단순 결합하는 방식 대신, 모달리티별 깊이를 다르게 둘 수 있는 2-스트림 교차 어텐션 구조를 정립.

## 한계 & 연결
외부 객체 탐지기(Faster R-CNN) 전처리에 강하게 의존해 느리고 범용성이 제한 → End-to-end 대조학습 **CLIP**으로 전환.
