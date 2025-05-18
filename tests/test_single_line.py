import unittest
import sys
import os

# 动态添加项目根目录到 sys.path，确保 src 模块可被找到
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from src.code_runner import CodeRunner

class TestSingleLineCode(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """初始化 CodeRunner 实例"""
        cls.runner = CodeRunner()

    def test_single_line_execution(self):
        """测试单行代码执行"""
        code = "print('Hello SAI run!')"
        # 调用 run_code 并获取结果
        result = self.runner.run_code(code)
        
        # 调试信息：打印 headers 和 token（注意：不打印实际 CA 令牌值以保护隐私）
        headers = self.runner.headers
        print(f"调试信息 - Headers: {{'Content-Type': '{headers.get('Content-Type')}', 'ca': {'<present>' if 'ca' in headers else '<not set>'}}}")
        from src.token_generator import generate_token
        token = generate_token(code)
        print(f"调试信息 - 生成的 Token: {token}")
        print(f"调试信息 - API 响应: {result}")
        
        # 打印代码运行的实际输出
        print(f"代码运行结果: {result.get('output', '无输出')}")
        
        # 断言检查
        self.assertTrue(result.get("success"), f"执行失败: {result.get('output')}")
        self.assertIn("Hello SAI run!", result.get("output"), "输出应包含预期字符串")

if __name__ == "__main__":
    unittest.main()