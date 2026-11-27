---
id: prophet
short: "Prophet"
title: "Forecasting at Scale"
year: 2017
venue: "Taylor & Letham (Facebook) / The American Statistician 2018"
category: "Time Series"
tags: ["Additive Model", "Trend Changepoint", "Fourier Seasonality", "Interpretable"]
pdf: "논문/Time Series/prophet.pdf"
predecessors: ["arima"]
successors: []
---

## 한 줄 요약
시계열을 추세(구간 선형/로지스틱) + 다중 계절성(푸리에 급수) + 휴일 효과의 가법 모델로 분해해, 비전문가도 해석·튜닝하기 쉽게 만든 실무형 예측 모델.

## 핵심 메커니즘
- y(t) = g(t)[추세+변화점] + s(t)[연/주/일 푸리에 계절성] + h(t)[휴일/이벤트] + ε_t 의 가법(GAM) 구조.
- 희소 사전분포(Laplace)로 추세 변화점(changepoint)을 자동 감지하고, 결측치·이상치에도 강건.
- 도메인 지식을 용량 상한(carrying capacity)·휴일 목록·변화점 민감도 같은 직관적 파라미터로 직접 반영.

## 기존 대비 차이
ARIMA처럼 까다로운 정상성 검정·차수(p,d,q) 튜닝이나 균일 간격 데이터가 필요 없고, 다중 계절성과 비즈니스 이벤트 반영이 압도적으로 쉬움.

## 한계 & 연결
시간 t 자체의 곡선 피팅 방식이라 강한 단기 자기상관(lag)이나 복잡한 다변량 시계열 상호작용 예측에서는 ARIMA/딥러닝보다 약할 수 있음.
