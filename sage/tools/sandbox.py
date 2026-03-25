SAFE_IMPORTS = [
    "json", "datetime", "re", "math",
    "collections", "itertools", "hashlib",
]

BLOCKED_PATTERNS = [
    "import os", "import subprocess", "import sys",
    "exec(", "eval(", "__import__",
    "rm ", "DROP ", "TRUNCATE", "DELETE FROM",
    "shutil", "os.system", "os.remove",
]

def validate_code(code: str) -> str:
    """2차 방어선: AST 파싱 이전 문자열 레벨 차단"""
    code_lower = code.lower()
    for pattern in BLOCKED_PATTERNS:
        if pattern.lower() in code_lower:
            raise ValueError(f"🚫 차단된 패턴 감지: '{pattern}'")
    return code
