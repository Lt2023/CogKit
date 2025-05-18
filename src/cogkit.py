import requests
import aiohttp
import json
import asyncio
import base64
from .token import generate_token
from .config import load_config

class CogKit:
    """CogKit 类用于简化 SAI API 的调用"""
    
    def __init__(self):
        """初始化 CogKit，加载配置并设置基本参数"""
        self.config = load_config()
        self.base_url = "https://ai.coludai.cn"
        self.coderunner_url = "https://reasoner.coludai.cn"
        self.headers = {
            'ca': self.config.get('COGKIT_CA_TOKEN', ''),
            'Content-Type': 'application/json'
        }

    def _make_request(self, url, payload):
        """执行同步 POST 请求"""
        try:
            response = requests.post(url, headers=self.headers, data=json.dumps(payload))
            response.raise_for_status()
            return response.json()
        except Exception as e:
            raise Exception(f"API 请求失败：{str(e)}")

    async def _make_async_request(self, url, payload):
        """执行异步 POST 请求"""
        async with aiohttp.ClientSession() as session:
            async with session.post(url, headers=self.headers, data=json.dumps(payload)) as response:
                if response.status != 200:
                    raise Exception(f"异步 API 请求失败：{response.status}")
                return await response.json()

    def chat_l6(self, prompt, stream=False, sessionid=None):
        """调用 SAI-Chat-L6 API"""
        url = f"{self.base_url}/api/chat"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        return self._make_request(url, payload)

    async def chat_l6_async(self, prompt, stream=False, sessionid=None):
        """异步调用 SAI-Chat-L6 API"""
        url = f"{self.base_url}/api/chat"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        return await self._make_async_request(url, payload)

    def reasoner3mini(self, prompt, use_network=False, stream=False, sessionid=None):
        """调用 SAI-Reasoner3mini API，支持 Thinking 和 SearchResults"""
        url = f"{self.coderunner_url}/api/illation"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "use_network": use_network, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        result = self._make_request(url, payload)
        # 确保返回包含 output、Thinking 和 SearchResults（如果联网）
        return {
            "output": result.get("output", ""),
            "Thinking": result.get("Thinking", ""),
            "SearchResults": result.get("SearchResults", []) if use_network else []
        }

    async def reasoner3mini_async(self, prompt, use_network=False, stream=False, sessionid=None):
        """异步调用 SAI-Reasoner3mini API，支持 Thinking 和 SearchResults"""
        url = f"{self.coderunner_url}/api/illation"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "use_network": use_network, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        result = await self._make_async_request(url, payload)
        # 确保返回包含 output、Thinking 和 SearchResults（如果联网）
        return {
            "output": result.get("output", ""),
            "Thinking": result.get("Thinking", ""),
            "SearchResults": result.get("SearchResults", []) if use_network else []
        }

    def img_desc(self, image_url):
        """调用 SAI-img_desc API，使用图片 URL"""
        url = f"{self.base_url}/api/img_desc"
        # 下载图片
        try:
            response = requests.get(image_url)
            response.raise_for_status()
            file_data = response.content
        except Exception as e:
            raise Exception(f"下载图片失败：{str(e)}")
        # 将图片数据转换为 Base64 编码
        file_base64 = base64.b64encode(file_data).decode('utf-8')
        # 生成 token，基于图片 URL
        token = generate_token(image_url, "text")
        # 构造 payload
        payload = {
            "file": file_base64,
            "token": token
        }
        return self._make_request(url, payload)

    def tts(self, text):
        """调用 SAI-tts API"""
        url = f"{self.base_url}/api/tts"
        token = generate_token(text, "text")
        payload = {"text": text, "token": token}
        return self._make_request(url, payload)

    async def tts_async(self, text):
        """异步调用 SAI-tts API"""
        url = f"{self.base_url}/api/tts"
        token = generate_token(text, "text")
        payload = {"text": text, "token": token}
        return await self._make_async_request(url, payload)

    def txt2img(self, text, negative_prompt=None):
        """调用 SAI-txt2img API"""
        url = f"{self.base_url}/api/txt2img"
        token = generate_token(text, "text")
        payload = {"text": text, "token": token}
        if negative_prompt:
            payload["negative_prompt"] = negative_prompt
        return self._make_request(url, payload)

    async def txt2img_async(self, text, negative_prompt=None):
        """异步调用 SAI-txt2img API"""
        url = f"{self.base_url}/api/txt2img"
        token = generate_token(text, "text")
        payload = {"text": text, "token": token}
        if negative_prompt:
            payload["negative_prompt"] = negative_prompt
        return await self._make_async_request(url, payload)

    def coder(self, prompt, stream=False, sessionid=None, sysprompt=None):
        """调用 SAI-Coder API"""
        url = f"{self.base_url}/api/chat/coder"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        if sysprompt:
            payload["sysprompt"] = sysprompt
        return self._make_request(url, payload)

    async def coder_async(self, prompt, stream=False, sessionid=None, sysprompt=None):
        """异步调用 SAI-Coder API"""
        url = f"{self.base_url}/api/chat/coder"
        token = generate_token(prompt, "prompt")
        payload = {"prompt": prompt, "token": token, "stream": stream}
        if sessionid:
            payload["sessionid"] = sessionid
        if sysprompt:
            payload["sysprompt"] = sysprompt
        return await self._make_async_request(url, payload)

    def run_code(self, code):
        """调用 CodeRunner API"""
        url = f"{self.coderunner_url}/api/run_code/python"
        token = generate_token(code, "code")
        payload = {"code": code, "token": token}
        return self._make_request(url, payload)

    async def run_code_async(self, code):
        """异步调用 CodeRunner API"""
        url = f"{self.coderunner_url}/api/run_code/python"
        token = generate_token(code, "code")
        payload = {"code": code, "token": token}
        return await self._make_async_request(url, payload)

    def chat_l6_batch(self, prompts, stream=False):
        """批量调用 SAI-Chat-L6 API"""
        return [self.chat_l6(prompt, stream) for prompt in prompts]

    def reasoner3mini_batch(self, prompts, use_network=False, stream=False):
        """批量调用 SAI-Reasoner3mini API"""
        return [self.reasoner3mini(prompt, use_network, stream) for prompt in prompts]

    def coder_batch(self, prompts, stream=False):
        """批量调用 SAI-Coder API"""
        return [self.coder(prompt, stream) for prompt in prompts]

    def run_code_batch(self, codes):
        """批量调用 CodeRunner API"""
        return [self.run_code(code) for code in codes]