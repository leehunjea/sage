import os
from smolagents import CodeAgent, OpenAIServerModel
from smolagents.local_python_executor import LocalPythonExecutor
from sage.tools.sandbox import SAFE_IMPORTS
from sage.observability.tracer import init_tracing

def create_agent(tools: list = None, max_steps: int = 15) -> CodeAgent:
    init_tracing()

    model = OpenAIServerModel(
        model_id=os.environ.get("MODEL_NAME", "qwen3.5-27b"),
        api_base=f"http://localhost:{os.environ.get('VLLM_PORT', '8000')}/v1",
        api_key="EMPTY",
        max_tokens=32768,
        temperature=0.6,
        top_p=0.95,
        presence_penalty=0.0,
        extra_body={
            "top_k": 20,
            "chat_template_kwargs": {"enable_thinking": True},
        },
    )

    executor = LocalPythonExecutor(
        additional_authorized_imports=SAFE_IMPORTS,
        max_print_outputs_length=5000,
    )

    return CodeAgent(
        tools=tools or [],
        model=model,
        executor=executor,
        additional_authorized_imports=SAFE_IMPORTS,
        max_steps=max_steps,
    )
