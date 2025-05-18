import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.cogkit import CogKit

def main():
    """示例：调用 SAI-Reasoner3mini API，处理 Thinking 和 SearchResults"""
    # 初始化 CogKit
    cogkit = CogKit()
    
    # 执行推理请求（启用联网）
    result = cogkit.reasoner3mini(prompt="分析全球变暖的影响", use_network=True)
    
    # 输出结果
    print("SAI-Reasoner3mini 思考过程：", result.get("Thinking", "无思考过程"))
    print("SAI-Reasoner3mini 输出：", result.get("output", "无输出"))
    if result.get("SearchResults"):
        print("联网搜索结果：")
        for item in result.get("SearchResults", []):
            print(f"- {item.get('name', '无标题')}: {item.get('snippet', '无摘要')}")

if __name__ == "__main__":
    main()