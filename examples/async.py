import sys
import os
# 动态添加项目根目录到 sys.path，确保 src 模块可导入
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import asyncio
from src.client import CogKitRunner

async def main():
    """异步调用示例：异步运行 Python 代码"""
    try:
        runner = CogKitRunner()
        code = "print('Async SAI run!')"
        result = await runner.run_code_async(code)
        print("输出:", result.get("output"))
        print("成功:", result.get("success"))
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    asyncio.run(main())