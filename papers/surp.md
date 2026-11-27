---
id: surp
short: "SURP v1.0"
title: "SURP: Extraction of Robotic Surface Processing Strategies from Human Demonstrations"
year: 2025
venue: "DLR / IROS 2025"
category: "Dataset & Robustness"
tags: ["Surface Processing", "Sanding", "Force-Torque", "Human Demo", "Strategy"]
pdf: "논문/Dataset/SURP-v1.0.pdf"
predecessors: ["forcevla"]
successors: ["maia-cria"]
---

## 한 줄 요약
21명의 전동 샌딩 인간 시연(4종 형상 × 84궤적)에서 경로·접촉력 전략을 추출하기 위해 영상·자세·6축 F/T를 공개한 표면가공 데이터셋.

## 핵심 메커니즘
- 공구 조작 방해를 피하기 위해 Vive 트래커로 공구 자세를 측정하고, F/T 센서는 작업물 하단에 배치.
- 단순 궤적 모방이 아니라 작업자 간 공통 전략(snake, zigzag, circle 등)과 법선력(42~46N) 추출을 목표.
- 가이드 코트 제거 여부로 표면 커버리지를 검증.

## 기존 대비 차이
픽앤플레이스 중심 로봇 데이터셋과 달리, 연속 접촉력 유지가 필수인 산업 샌딩(표면가공) 전략 분석에 특화.

## 한계 & 연결
인간 도구 pose여서 로봇 리타게팅 필요, 불규칙 샘플링(83~470Hz)·트래킹 갭 존재. (Heart-Lab에서 CRIA와 통합 LeRobot 328ep 검증 완료)
