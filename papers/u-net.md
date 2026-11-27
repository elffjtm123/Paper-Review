---
id: u-net
short: "U-Net"
title: "U-Net: Convolutional Networks for Biomedical Image Segmentation"
year: 2015
venue: "Ronneberger et al. / MICCAI 2015"
category: "Vision"
tags: ["Segmentation", "Skip Connection", "Encoder-Decoder", "Dense Prediction"]
pdf: "논문/Vision/U-Net.pdf"
predecessors: ["autoencoder", "r-cnn"]
successors: ["ddpm"]
---

## 한 줄 요약
대칭형 축소(Encoder)-확장(Decoder) 경로 사이를 같은 해상도끼리 Skip Connection으로 연결해, 적은 데이터로도 픽셀 단위 정밀 분할을 해낸 대표 아키텍처.

## 핵심 메커니즘
- Contracting path(다운샘플링)로 전역 문맥(무엇인가)을 잡고, Expanding path(업샘플링)로 위치(어디인가)를 복원.
- 인코더의 고해상도 특징맵을 디코더 대응 층에 채널 결합(Skip Connection)해 공간 디테일 손실 복구.
- 탄성 변형(elastic deformation) 증강과 경계 가중 손실로 소량 의료 영상에서도 높은 정확도 달성.

## 기존 대비 차이
단순 AutoEncoder/FCN이 업샘플링 과정에서 경계가 뭉개지던 문제를 다단계 Skip Connection으로 해결 → 이후 **DDPM** 디노이징 백본의 표준으로 채택.

## 한계 & 연결
합성곱의 국소 수용야(receptive field) 한계로 초장거리 전역 문맥 모델링에는 Self-Attention 결합이나 **DiT**가 유리.
