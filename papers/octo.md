---
id: octo
short: "Octo"
title: "Octo: An Open-Source Generalist Robot Policy"
year: 2024
venue: "UC Berkeley / RSS 2024"
category: "VLA"
tags: ["Generalist Policy", "Diffusion Head", "Open-Source", "Readout Tokens"]
pdf: "논문/VLA/Octo.pdf"
predecessors: ["rt-x", "ddpm", "transformer"]
successors: ["openvla", "pi-0"]
---

## 한 줄 요약
OXE 80만 궤적으로 사전학습하고 Diffusion 액션 헤드와 블록 어텐션으로 새로운 센서·행동 공간에 빠르게 미세조정 가능한 경량 오픈소스 범용 로봇 정책.

## 핵심 메커니즘
- 언어 지시·목표 이미지·다중 카메라·고유수용감각을 모듈형 토큰으로 조합하고 Readout 토큰으로 집약.
- 이산 토큰 대신 경량 Diffusion Action Head로 연속 다봉(multimodal) 액션 청크 예측.
- 소형(27M)·기본(93M) 크기로 단일 소비자 GPU에서도 새 로봇·액션 공간 미세조정 가능.

## 기존 대비 차이
대형 VLM 백본을 쓰는 RT-2·OpenVLA보다 훨씬 가볍고 유연하며, 카메라 추가·관절 공간 변경 같은 구조 변화 적응성이 뛰어남.

## 한계 & 연결
VLM 사전학습이 없어 복잡한 자연어·오픈월드 의미 추론이 약함. (Heart-Lab LIBERO-Object 재현: 100k step 84.0%)
