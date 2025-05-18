import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.cogkit import CogKit

def main():
    """示例：调用 SAI-Chat-L6 API"""
    # 初始化 CogKit
    cogkit = CogKit()
    
    # 执行聊天请求
    result = cogkit.chat_l6(prompt="你是谁？")
    print("SAI-Chat-L6 响应：", result.get("output", "无输出"))

if __name__ == "__main__":
    main()