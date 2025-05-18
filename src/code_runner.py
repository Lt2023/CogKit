import requests
from .token_generator import generate_token
from dotenv import load_dotenv
import os

class CodeRunner:
    """CogKit API 客户端，用于运行 Python 代码"""
    def __init__(self):
        # 加载 .env 文件中的环境变量
        load_dotenv()
        self.base_url = "https://coderunner.coludai.cn/api/run_code/python"
        self.headers = {
            "Content-Type": "application/json"
        }
        # 如果 .env 中有 CA 令牌且不是默认值，添加到 headers
        ca_token = os.getenv("CA_TOKEN")
        if ca_token and ca_token != "your-ca-token-here":
            self.headers["ca"] = ca_token
    
    def run_code(self, code: str) -> dict:
        """使用 CogKit API 运行 Python 代码"""
        # 生成 token
        token = generate_token(code)
        payload = {
            "code": code,
            "token": token
        }
        
        try:
            # 发送 POST 请求
            response = requests.post(self.base_url, json=payload, headers=self.headers)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            # 处理网络错误
            return {"success": False, "output": f"错误: {str(e)}"}