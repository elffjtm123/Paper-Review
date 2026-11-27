---
id: dino
short: "DINO"
title: "Emerging Properties in Self-Supervised Vision Transformers"
year: 2021
venue: "Caron et al. (Meta) / ICCV 2021"
category: "Multimodal"
tags: ["Self-Distillation", "ViT", "No Labels", "EMA Teacher", "Semantic Segmentation"]
pdf: "논문/Multimodal/DiNO.pdf"
predecessors: ["vit"]
successors: ["dinov2"]
---

## 한 줄 요약
라벨도 대조 음성샘플도 없이 Student-Teacher 자기증류(EMA)로 ViT를 학습했더니, 어텐션 맵에 객체 분할(segmentation) 특성이 자연 창발함을 보인 연구.

## 핵심 메커니즘
- Multi-crop(전역 2개 + 지역 크롭 다수): Student는 모든 크롭을 보고, EMA Teacher는 전역 크롭만 봐서 '부분→전체' 대응 학습.
- Negative pair 없이 붕괴(collapse)를 막기 위해 Teacher 출력에 **Centering**(평균 빼기)과 **Sharpening**(낮은 온도) 적용.
- 지도학습 ViT나 CNN에선 안 나타나던 선명한 객체 경계 어텐션과 높은 k-NN 분류 성능이 자발적으로 등장.

## 기존 대비 차이
대규모 텍스트 쌍(CLIP)이나 음성샘플(MoCo/SimCLR) 없이 순수 자기지도 ViT만으로 강력한 공간·객체 중심 특징을 획득.

## 한계 & 연결
ImageNet 규모 데이터셋에 한정되어 범용 파운데이션 백본으로 스케일링하기엔 부족 → **DINOv2**로 대규모 큐레이션·확장.
