import requests
import aiohttp
import logging
import json
from typing import Dict, List, Optional
from .token import generate_token
from .config import load_config

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CogKitAPIError(Exception):
    """CogKit API 调用异常"""
    pass

class CogKitRunner:
    """CogKit 代码运行客户端，用于调用 /run_code/python 接口"""
    
    def __init__(self, ca_token: Optional[str] = None, base_url: str = "https://coderunner.coludai.cn"):
        """
        初始化 CogKitRunner 客户端

        参数:
            ca_token (str, optional): 团队 CA 令牌，如果为空则从环境变量加载
            base_url (str): API 基础地址，默认为 https://coderunner.coludai.cn
        """
        self.ca_token = ca_token or load_config().get("COGKIT_CA_TOKEN")
        if not self.ca_token:
            raise ValueError("必须提供 CA 令牌")
        self.base_url = base_url.rstrip('/')
        self.headers = {
            "ca": self.ca_token,
            "Content-Type": "application/json"
        }

    def run_code(self, code: str) -> Dict[str, any]:
        """
        同步运行 Python 代码

        参数:
            code (str): 要执行的 Python 代码

        返回:
            Dict[str, any]: API 响应，包含 'output' 和 'success'

        异常:
            CogKitAPIError: 如果 API 调用失败
        """
        date_hash, token = generate_token(code)
        logger.info(f"生成 token: {token} (日期哈希: {date_hash})")
        
        payload = {"code": code, "token": token}
        url = f"{self.base_url}/api/run_code/python"
        
        try:
            response = requests.post(url, json=payload, headers=self.headers)
            response.raise_for_status()
            # 尝试解析响应为 JSON，即使内容类型不是 application/json
            content_type = response.headers.get('Content-Type', '')
            try:
                result = json.loads(response.text)
                logger.info(f"API 响应: {result}")
                return result
            except json.JSONDecodeError:
                raise CogKitAPIError(f"无法解析 JSON，内容类型: {content_type}, 响应: {response.text}")
        except requests.RequestException as e:
            logger.error(f"API 请求失败: {e}")
            raise CogKitAPIError(f"运行代码失败: {str(e)}")

    async def run_code_async(self, code: str) -> Dict[str, any]:
        """
        异步运行 Python 代码

        参数:
            code (str): 要执行的 Python 代码

        返回:
            Dict[str, any]: API 响应，包含 'output' 和 'success'

        异常:
            CogKitAPIError: 如果 API 调用失败
        """
        date_hash, token = generate_token(code)
        logger.info(f"生成 token: {token} (日期哈希: {date_hash})")
        
        payload = {"code": code, "token": token}
        url = f"{self.base_url}/api/run_code/python"
        
        async with aiohttp.ClientSession(headers=self.headers) as session:
            try:
                async with session.post(url, json=payload) as response:
                    if response.status != 200:
                        raise CogKitAPIError(f"API 错误: {response.status} - {await response.text()}")
                    # 尝试解析响应为 JSON，即使内容类型不是 application/json
                    content_type = response.headers.get('Content-Type', '')
                    text = await response.text()
                    try:
                        result = json.loads(text)
                        logger.info(f"异步 API 响应: {result}")
                        return result
                    except json.JSONDecodeError:
                        raise CogKitAPIError(f"无法解析 JSON，内容类型: {content_type}, 响应: {text}")
            except aiohttp.ClientError as e:
                logger.error(f"异步请求失败: {e}")
                raise CogKitAPIError(f"运行代码失败: {str(e)}")

    def run_code_batch(self, codes: List[str]) -> List[Dict[str, any]]:
        """
        批量运行多段 Python 代码

        参数:
            codes (List[str]): 要执行的 Python 代码列表

        返回:
            List[Dict[str, any]]: 每段代码的 API 响应列表
        """
        results = []
        for code in codes:
            try:
                result = self.run_code(code)
                results.append(result)
            except CogKitAPIError as e:
                results.append({"output": str(e), "success": False})
        return results