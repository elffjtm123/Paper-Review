---
id: rt-1
short: "RT-1"
title: "RT-1: Robotics Transformer for Real-World Control at Scale"
year: 2022
venue: "Google Robotics / RSS 2023"
category: "VLA"
tags: ["VLA", "TokenLearner", "FiLM", "Action Tokenization", "Real-time"]
pdf: "논문/VLA/RT-1.pdf"
predecessors: ["transformer"]
successors: ["rt-2", "rt-x", "octo"]
---

## 한 줄 요약
시각(FiLM-EfficientNet) + TokenLearner 압축 + Decoder Transformer로 13만 실제 시연을 단일 정책으로 학습한 초기 대규모 로봇 트랜스포머.

## 핵심 메커니즘
- FiLM-EfficientNet-B3로 자연어 지시에 조건화된 시각 특징을 추출.
- TokenLearner로 프레임당 81개 시각 토큰을 8개로 압축해 3Hz 실시간 추론(35M 파라미터) 달성.
- 로봇 행동(팔 7DoF + 베이스 3DoF + 모드)을 256구간 이산 토큰으로 양자화해 자기회귀 생성.

## 기존 대비 차이
작업별 소규모 정책을 따로 학습하던 기존 모방학습과 달리, 700+ 작업을 하나의 Transformer 정책으로 스케일링해 미지 작업·배경 일반화를 보임.

## 한계 & 연결
웹 규모 VLM 사전학습 지식이 없어 완전히 새로운 개념·추론 일반화에 한계 → **RT-2**로 확장. (Heart-Lab 온디바이스 경량화 연구노트 분석 대상)
