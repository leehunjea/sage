from dotenv import load_dotenv
load_dotenv()

from sage.core.agent import create_agent

agent = create_agent(tools=[], max_steps=10)

def run(prompt: str):
    print(f"\n🤖 SAGE 태스크 시작\n{'─'*40}")
    result = agent.run(prompt)
    print(f"{'─'*40}\n✅ 결과: {result}\n")
    return result

if __name__ == "__main__":
    run("""
    1. 1부터 100까지의 소수(Prime number)를 구해.
    2. 가장 큰 소수와 가장 작은 소수의 차이를 계산해서 반환해줘.
    """)
