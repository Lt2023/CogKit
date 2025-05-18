import hashlib
from datetime import datetime

def generate_token(input_text, input_type):
    """生成 API 所需的令牌
    
    Args:
        input_text (str): 输入文本（如 prompt 或 code）
        input_type (str): 输入类型（'prompt', 'text', 或 'code'）
    
    Returns:
        str: 生成的 MD5 令牌
    """
    # 获取当前日期，格式为 YYYY-MM-DD
    current_date = datetime.now().strftime("%Y-%m-%d")
    
    # 对日期进行 MD5 加密，取前 6 位
    date_hash = hashlib.md5(current_date.encode()).hexdigest()[:6]
    
    # 组合输入文本和日期哈希
    combined = f"{input_text}{date_hash}"
    
    # 生成最终令牌
    token = hashlib.md5(combined.encode()).hexdigest()
    
    return token