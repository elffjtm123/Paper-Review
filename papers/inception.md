---
id: inception
short: "Inception (GoogLeNet)"
title: "Going Deeper with Convolutions"
year: 2014
venue: "Szegedy et al. (Google) / CVPR 2015"
category: "Vision"
tags: ["Multi-Scale", "1x1 Bottleneck", "Efficiency", "CNN"]
pdf: "논문/Vision/Inception.pdf"
predecessors: []
successors: ["batchnorm", "resnet"]
---

## 한 줄 요약
한 층 안에서 1×1·3×3·5×5 합성곱과 풀링을 병렬 결합(Inception 모듈)하고 1×1 병목으로 차원을 압축해, 적은 파라미터로 22층 심층 CNN을 구현.

## 핵심 메커니즘
- Inception 모듈: 다양한 크기의 객체를 동시에 포착하기 위해 멀티스케일 필터를 병렬 적용 후 채널 결합.
- 3×3·5×5 직전에 **1×1 Convolution**으로 채널 차원을 줄여 연산량 폭증을 차단(AlexNet 대비 파라미터 1/12).
- 중간층 보조 분류기(Auxiliary Classifiers)로 22층 깊은 망의 기울기 전파 보조 + Global Average Pooling으로 FC 제거.

## 기존 대비 차이
단순히 필터를 크게·층을 무작정 두껍게 쌓던 VGG 등과 달리, 1×1 병목과 멀티스케일 병렬 구조로 연산 효율과 정확도를 동시 달성.

## 한계 & 연결
구조가 복잡해 하이퍼파라미터 수정이 까다롭고, 더 깊은 망(50~152층)에서는 기울기 퇴화 문제가 남음 → **ResNet**의 잔차 연결로 돌파.
