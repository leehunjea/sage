import os
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import SimpleSpanProcessor
from langfuse.opentelemetry import LangfuseSpanExporter
from smolagents.integrations.opentelemetry import SmolagentsInstrumentor

_initialized = False

def init_tracing():
    global _initialized
    if _initialized:
        return
    tracer_provider = TracerProvider()
    tracer_provider.add_span_processor(
        SimpleSpanProcessor(LangfuseSpanExporter())
    )
    SmolagentsInstrumentor().instrument(tracer_provider=tracer_provider)
    _initialized = True
    print("✅ Langfuse 트레이싱 초기화 완료")
