import hashlib
from datetime import datetime

def generate_token(code: str) -> tuple[str, str]:
    """
    根据当前日期和代码生成token

    步骤:
    1. 获取当前日期（格式: YYYY-MM-DD）
    2. 对日期进行MD5加密，取前6位
    3. 将代码与日期哈希拼接，再进行MD5加密，得到最终token

    参数:
        code (str): 要执行的Python代码

    返回:
        tuple[str, str]: (日期哈希, 最终token)
    """
    current_date = datetime.now().strftime("%Y-%m-%d")
    date_hash = hashlib.md5(current_date.encode()).hexdigest()[:6]
    combined = f"{code}{date_hash}"
    final_token = hashlib.md5(combined.encode()).hexdigest()
    return date_hash, final_token

def verify_token(code: str, token: str) -> bool:
    """
    验证提供的token是否对给定代码有效

    参数:
        code (str): Python代码
        token (str): 要验证的token

    返回:
        bool: 如果token有效则返回True，否则返回False
    """
    _, expected_token = generate_token(code)
    return token == expected_token