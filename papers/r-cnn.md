---
id: r-cnn
short: "R-CNN"
title: "Rich Feature Hierarchies for Accurate Object Detection and Semantic Segmentation"
year: 2014
venue: "Girshick et al. / CVPR 2014"
category: "Vision"
tags: ["Object Detection", "Region Proposal", "Two-Stage", "CNN"]
pdf: "논문/Vision/R-CNN.pdf"
predecessors: []
successors: ["u-net", "vilbert"]
---

## 한 줄 요약
Selective Search로 뽑은 약 2,000개 후보 영역(Region Proposal)마다 CNN 특징을 추출해 SVM 분류·박스 회귀를 수행, 딥러닝 객체 탐지 시대를 연 논문.

## 핵심 메커니즘
- Selective Search로 클래스 무관 후보 영역 ~2,000개 생성 후 고정 크기로 warp.
- ImageNet 사전학습 CNN으로 각 영역 특징 추출(도메인 미세조정) → 클래스별 선형 SVM 분류 + Bounding-box 회귀.
- 기존 HOG/SIFT 기반 탐지기 대비 PASCAL VOC mAP를 30% 이상 대폭 끌어올림.

## 기존 대비 차이
분류 중심이던 CNN을 '후보 영역 추출 + CNN 특징 분류' 2단계 파이프라인으로 객체 탐지까지 성공적으로 확장.

## 한계 & 연결
2,000개 영역마다 CNN을 따로 돌려 극도로 느리고(이미지당 수십 초) 다단계 분리 학습 필요 → Fast/Faster R-CNN으로 발전.
