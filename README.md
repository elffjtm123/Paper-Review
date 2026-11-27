# Heart-Lab 논문 지식베이스 (63편)

초압축 4칸 기록 노트(`papers/*.md`)를 유일한 원본으로 삼아 복습 웹앱·매일 퀴즈·3축 논문 추천·RAG 검색을 구동합니다.

## 도메인 분포

| 도메인 | 편수 | 논문 |
|---|---:|---|
| VLA | 15 | [RT-1](papers/rt-1.md), [PaLM-E](papers/palm-e.md), [RT-2](papers/rt-2.md), [RT-X (OXE)](papers/rt-x.md), [Octo](papers/octo.md), [OpenVLA](papers/openvla.md), [Pi-0](papers/pi-0.md), [OpenVLA-OFT](papers/openvla-oft.md), [FAST](papers/fast.md), [Pi-0.5](papers/pi-0-5.md), [GR00T N1](papers/groot-n1.md), [SmolVLA](papers/smolvla.md), [WALL-OSS](papers/wall-oss.md), [ForceVLA](papers/forcevla.md), [StableVLA](papers/stablevla.md) |
| Generative | 9 | [AutoEncoder](papers/autoencoder.md), [VAE](papers/vae.md), [GAN](papers/gan.md), [CGAN](papers/cgan.md), [DCGAN](papers/dcgan.md), [Real NVP](papers/real-nvp.md), [DDPM](papers/ddpm.md), [DiT](papers/dit.md), [Flow Matching](papers/flow-matching.md) |
| Transformer & LLM | 8 | [Transformer](papers/transformer.md), [GPT-1](papers/gpt-1.md), [BERT](papers/bert.md), [RoPE](papers/rope.md), [PaLM](papers/palm.md), [NoPE](papers/transformer-without-pe.md), [LLaMA](papers/llama.md), [LLaDA (Diffusion LLM)](papers/diffusion-llm.md) |
| Optimization | 7 | [BatchNorm](papers/batchnorm.md), [LayerNorm](papers/layernorm.md), [LoRA](papers/lora.md), [FlashAttention](papers/flashattention.md), [QLoRA](papers/qlora.md), [PagedAttention (vLLM)](papers/pagedattention.md), [DoRA](papers/dora.md) |
| Dataset & Robustness | 5 | [SURP v1.0](papers/surp.md), [LIBERO-Plus](papers/libero-plus.md), [LIBERO-PRO](papers/libero-pro.md), [MAIA (CRIA)](papers/maia-cria.md), [RobustVLA](papers/robustvla.md) |
| Multimodal | 5 | [ViLBERT](papers/vilbert.md), [CLIP](papers/clip.md), [DINO](papers/dino.md), [DINOv2](papers/dinov2.md), [SigLIP](papers/siglip.md) |
| Vision | 5 | [R-CNN](papers/r-cnn.md), [Inception (GoogLeNet)](papers/inception.md), [U-Net](papers/u-net.md), [ResNet](papers/resnet.md), [ViT](papers/vit.md) |
| Sequence & Audio | 5 | [LSTM](papers/lstm.md), [LSTM + Forget Gate](papers/lstm-forget-gate.md), [Bi-LSTM](papers/bi-lstm.md), [GRU](papers/gru.md), [WaveNet](papers/wavenet.md) |
| Robot Control | 2 | [ACT (ALOHA)](papers/act.md), [cuRobo](papers/curobo.md) |
| Time Series | 2 | [ARIMA](papers/arima.md), [Prophet](papers/prophet.md) |

## 실행 방법

- `python3 build.py` : `papers/*.md` 수정 후 인덱스/정적 번들 갱신
- `python3 server.py` : 로컬 + 휴대폰 접속 서버 실행 (포트 `8765`)
- 매일 오전 8:00 `launchd` 자동 기동 → 오늘의 퀴즈 완료 시 자동 종료
