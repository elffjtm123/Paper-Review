---
id: curobo
short: "cuRobo"
title: "cuRobo: Parallelized Collision-Free Minimum-Jerk Robot Motion Generation"
year: 2023
venue: "NVIDIA / ICRA 2024"
category: "Robot Control"
tags: ["Motion Planning", "GPU Parallel", "L-BFGS", "Collision-Free", "Minimum-Jerk"]
pdf: "논문/robot sim/cuRobo.pdf"
predecessors: []
successors: []
---

## 한 줄 요약
수많은 초기해를 GPU에서 병렬 최적화(IK → 입자 탐색 → L-BFGS)해 충돌 없고 부드러운(minimum-jerk) 로봇 팔 궤적을 30ms 내에 생성하는 모션 플래너.

## 핵심 메커니즘
- 관절 한계·속도/가속도/저크·자기충돌·환경충돌 제약을 페널티 비용항으로 바꿔 비볼록 전역 최적화로 정식화.
- 4단계 파이프라인: 병렬 충돌 회피 IK → 선형/기하 초기경로 → 입자 기반 탐색 + 병렬 L-BFGS 궤적 최적화 → 시간 스케일링.
- 병렬 잡음 선 탐색(line search)으로 GPU 분기를 최소화해 30ms급 실시간 생성 달성.

## 기존 대비 차이
기존 CPU 기반 모션 플래너(0.5~10초, 단일 초기해 국소최적 함정)를 GPU 대규모 병렬화로 10~100배 가속하면서 성공률까지 높임.

## 한계 & 연결
명시적 기하/충돌 모델(메시·복셀)이 필요해 비정형 물체나 접촉력 제어 작업에는 VLA/힘제어와 결합이 필요. (Heart-Lab 연구노트 정리 완료)
