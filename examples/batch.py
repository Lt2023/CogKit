import sys
import os
# 动态添加项目根目录到 sys.path，确保 src 模块可导入
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.client import CogKitRunner

def main():
    """批量执行示例：运行多段 Python 代码"""
    try:
        runner = CogKitRunner()
        codes = [
            "print('Task 1')",
            "print('Task 2')",
            "for i in range(3): print(i)"
        ]
        results = runner.run_code_batch(codes)
        for i, result in enumerate(results):
            print(f"代码 {i+1}: {result}")
    except Exception as e:
        print(f"错误: {str(e)}")

if __name__ == "__main__":
    main()