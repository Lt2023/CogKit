import hashlib
from datetime import datetime

def generate_token(code: str, date: str = None) -> str:
    """根据 CogKit API 规则生成 token"""
    # 步骤 1：如果未提供日期，获取当前日期
    if date is None:
        date = datetime.now().strftime("%Y-%m-%d")
    
    # 步骤 2：对日期进行 MD5 加密，取前 6 位
    date_md5 = hashlib.md5(date.encode()).hexdigest()[:6]
    
    # 步骤 3：将代码与 date_md5 拼接，再次进行 MD5 加密
    combined = code + date_md5
    token = hashlib.md5(combined.encode()).hexdigest()
    
    return token