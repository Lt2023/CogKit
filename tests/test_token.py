import unittest
from src.token_generator import generate_token

class TestTokenGenerator(unittest.TestCase):
    def test_token_generation(self):
        """测试 token 生成是否符合预期"""
        code = "print('Hello SAI run!')"
        date = "2025-05-18"
        token = generate_token(code, date)
        self.assertEqual(len(token), 32, "token 长度应为 32 位（MD5 哈希）")
        # 注意：MD5 是确定性的，可用已知值测试
        # 以下为示例 token，需根据 2025-05-18 实际计算
        # expected_token = "f0e8e4f1b7b2f8c0d3e9a6b5c4d2e1f0"
        # self.assertEqual(token, expected_token)

if __name__ == "__main__":
    unittest.main()