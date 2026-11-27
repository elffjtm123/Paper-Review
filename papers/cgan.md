---
id: cgan
short: "CGAN"
title: "Conditional Generative Adversarial Nets"
year: 2014
venue: "Mirza & Osindero / arXiv 2014"
category: "Generative"
tags: ["Conditional Generation", "GAN", "Class Conditioning"]
pdf: "논문/Generative Model/CGAN.pdf"
predecessors: ["gan"]
successors: ["dcgan", "dit"]
---

## 한 줄 요약
GAN의 생성자(G)와 판별자(D) 양쪽에 조건 정보 y(클래스 라벨 등)를 함께 입력해 원하는 속성의 데이터를 선택 생성하는 확장 모델.

## 핵심 메커니즘
- G(z, y)는 노이즈 z와 조건 y를 결합해 조건에 맞는 샘플을 생성.
- D(x, y)는 샘플이 진짜인지뿐 아니라 조건 y와 정합하는지까지 동시에 판별.
- 조건부 분포 p(x|y)를 직접 학습하는 일반적 프레임워크 제시.

## 기존 대비 차이
무작위 샘플만 뽑던 원조 GAN에 조건부 제어(controllability)를 도입해 텍스트→이미지·이미지 변환(pix2pix 등)의 토대를 마련.

## 한계 & 연결
원조 GAN의 학습 불안정성과 CNN 구조 부재 문제는 그대로 남아 있음 → **DCGAN**으로 구조 혁신.
