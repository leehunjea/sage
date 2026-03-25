#!/bin/bash
set -e

source .env

echo "🚀 SAGE vLLM 서버 기동 중..."
echo "모델: ${MODEL_NAME:-qwen3.5-27b}"
echo "포트: ${VLLM_PORT:-8000}"

# CUDA 12.8 라이브러리 경로
export LD_LIBRARY_PATH=/home/lhj/Desktop/sage/.venv/lib/python3.12/site-packages/nvidia/cu13/lib:/usr/local/cuda-13.0/targets/x86_64-linux/lib:$LD_LIBRARY_PATH

vllm serve Qwen/Qwen3.5-27B \
  --served-model-name ${MODEL_NAME:-qwen3.5-27b} \
  --port ${VLLM_PORT:-8000} \
  --gpu-memory-utilization 0.85 \
  --max-model-len 32768 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
