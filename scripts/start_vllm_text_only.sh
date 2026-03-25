#!/bin/bash
set -e

source .env

echo "🚀 SAGE vLLM 텍스트 전용 모드 기동 중..."
echo "비전 인코더 스킵 → 컨텍스트 65K 확장"

vllm serve Qwen/Qwen3.5-27B \
  --served-model-name ${MODEL_NAME:-qwen3.5-27b} \
  --port ${VLLM_PORT:-8000} \
  --gpu-memory-utilization 0.85 \
  --max-model-len 65536 \
  --reasoning-parser qwen3 \
  --enable-auto-tool-choice \
  --tool-call-parser qwen3_coder \
  --language-model-only
