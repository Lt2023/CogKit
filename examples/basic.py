from src.client import CogKitRunner

def main():
    """基本调用示例"""
    runner = CogKitRunner()
    code = "print('Hello SAI run!')"
    result = runner.run_code(code)
    print("输出:", result.get("output"))
    print("成功:", result.get("success"))

if __name__ == "__main__":
    main()