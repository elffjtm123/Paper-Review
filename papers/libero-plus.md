---
id: libero-plus
short: "LIBERO-Plus"
title: "LIBERO-Plus: In-depth Robustness Analysis of Vision-Language-Action Models"
year: 2025
venue: "OpenMOSS / CVPR 2026 (arXiv:2510.13626)"
category: "Dataset & Robustness"
tags: ["Benchmark", "VLA Robustness", "7-Axis Perturbation", "LIBERO"]
pdf: "논문/Dataset/LIBERO_Plus.pdf"
predecessors: ["openvla", "openvla-oft", "pi-0"]
successors: ["stablevla"]
---

## 한 줄 요약
LIBERO에 카메라·로봇 초기상태·언어·조명·배경·센서노이즈·물체배치 7차원 교란(10,030개 변형)을 체계적으로 주입해 VLA의 취약성을 해부한 벤치마크.

## 핵심 메커니즘
- 7가지 교란 축별로 기존 VLA(OpenVLA, π0, Octo 등)의 성공률 붕괴 패턴을 정량 진단.
- 클린 LIBERO에서 90%+ 나오던 모델들이 카메라 시점 변화나 초기 상태 교란에서 급락함을 입증.
- 교란 혼합 데이터 미세조정(OpenVLA-OFT+)의 효과와 한계(미지 교란 전이 부족) 제시.

## 기존 대비 차이
단순 클린 성공률 경쟁에 머물던 LIBERO 평가를 7축 다차원 스트레스 테스트로 확장해 강건성 연구 표준 벤치마크로 자리잡음.

## 한계 & 연결
Heart-Lab 재현 결과 π0의 경우 파일명 꼬리 지시문 영향과 센서 노이즈 재현 편차 등 평가 프로토콜 세밀 검증이 중요함을 확인.
