---
id: arima
short: "ARIMA"
title: "Time Series Analysis: Forecasting and Control (ARIMA / Box-Jenkins)"
year: 1970
venue: "Box & Jenkins (Classic Statistical Reference)"
category: "Time Series"
tags: ["Autoregressive", "Differencing", "Moving Average", "Stationarity"]
pdf: "논문/Time Series/ARIMA.pdf"
predecessors: []
successors: ["prophet"]
---

## 한 줄 요약
차분(I)으로 비정상 시계열을 정상화한 뒤 과거 값의 선형 결합(AR)과 과거 오차의 선형 결합(MA)으로 미래를 예측하는 고전 통계 시계열 표준 모델.

## 핵심 메커니즘
- ARIMA(p, d, q): d회 차분으로 추세 제거(정상성 확보) → 과거 p개 관측(AR) + 과거 q개 예측 오차(MA) 회귀.
- ACF/PACF 플롯과 AIC/BIC 기준으로 차수 (p, d, q)를 체계적으로 식별(Box-Jenkins 방법론).
- 계절성이 있으면 SARIMA로 확장.

## 기존 대비 차이
단순 이동평균·지수평활과 달리 자기상관과 비정상 추세를 수학적으로 정교하게 분해·추정하며, 소규모 단변량 시계열의 강력한 기준선.

## 한계 & 연결
선형·정상성 가정에 묶여 다중 계절성·휴일 효과·비선형 급변·결측치 처리가 까다로움 → 실무 친화형 **Prophet**이나 딥러닝 시계열로 확장.
