---
id: forcevla
short: "ForceVLA"
title: "ForceVLA: Enhancing VLA Models with a Force-aware MoE for Contact-Rich Manipulation"
year: 2025
venue: "arXiv 2025 (Dataset/Model Analysis)"
category: "VLA"
tags: ["Force Feedback", "6-Axis F/T", "Contact-Rich", "MoE", "LeRobot"]
pdf: "논문/VLA/ForceVLA.pdf"
predecessors: ["openvla", "pi-0"]
successors: ["surp", "maia-cria"]
---

## 한 줄 요약
시각·언어만으로 풀기 어려운 접촉 조작(삽입·닦기·필링)에 6축 힘/토크(F/T) 센서를 Force-aware MoE로 융합한 VLA와 접촉 데이터셋.

## 핵심 메커니즘
- RGB 2시점 + 언어 + 로봇 상태에 6축 힘/토크 시계열을 결합해 접촉 단계별 힘 피드백 제어.
- Force-aware MoE 라우터가 시각·힘 모달리티 비중을 접촉 국면에 따라 동적으로 조절.
- ForceVLA-Data: Flexiv Rizon 7-DOF VR 원격시연 244 에피소드(USB/플러그 삽입, 펌프, 필링, 보드 닦기), LeRobot v2.1 포맷 공개.

## 기존 대비 차이
시각 중심 VLA가 놓치는 미세 접촉력·저항 변화를 직접 입력으로 통합해 접촉 과업 성공률을 크게 향상.

## 한계 & 연결
고정밀 6축 F/T 센서 장착과 로봇별 좌표·스케일 캘리브레이션 의존. (Heart-Lab에서 SURP 인간 시연 데이터와 스키마·활용 비교 완료)
