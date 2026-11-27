---
id: clip
short: "CLIP"
title: "Learning Transferable Visual Models From Natural Language Supervision"
year: 2021
venue: "OpenAI / ICML 2021"
category: "Multimodal"
tags: ["Contrastive Learning", "Zero-Shot", "InfoNCE", "Dual Encoder"]
pdf: "논문/Multimodal/CLIP.pdf"
predecessors: ["vit", "resnet", "transformer", "vilbert"]
successors: ["siglip"]
---

## 한 줄 요약
4억 개의 웹 이미지-텍스트 쌍을 대조학습(InfoNCE)으로 정렬해, 미세조정 없이 자연어 프롬프트만으로 제로샷 시각 분류를 달성한 멀티모달 기초 모델.

## 핵심 메커니즘
- 이미지 인코더(ViT/ResNet)와 텍스트 인코더가 같은 임베딩 공간으로 투영.
- N×N 배치 유사도 행렬에서 대각선(정답 쌍) 코사인 유사도는 높이고 비대각선(오답 쌍)은 낮추는 대칭 Cross-Entropy 손실.
- 추론 시 클래스 이름을 'a photo of a {label}' 텍스트 임베딩으로 바꿔 제로샷 분류.

## 기존 대비 차이
고정 클래스 라벨(ImageNet 1,000종) 지도학습의 한계를 자연어 감독 신호로 깨고, 오픈-어휘(open-vocabulary) 시각 표현의 표준을 세움.

## 한계 & 연결
Softmax 대조손실이 거대한 배치 크기(32k)와 전체 GPU 간 동기화를 요구하며, 세밀한 공간·계수 추론은 약함 → **SigLIP**으로 개선.
