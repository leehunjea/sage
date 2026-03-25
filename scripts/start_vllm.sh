#!/bin/bash
set -e

source .env

echo "🚀 SAGE vLLM 서버 기동 중..."
echo "모델: ${MODEL_NAME:-qwen3.5-27b}"
echo "포트: ${VLLM_PORT:-8000}"

vllm serve Qwen/Qwen3.5-27B \
  --served-model-name ${MODEL_NAME:-qwen3.5-27b} \
  --port ${VLLM_PORT:-8000} \
  --gpu-memory-utilization 0.85 \
  --max-model-len 32768 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder
