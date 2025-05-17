import re

class ResultParser:
    """解析CogKit API返回的输出"""

    @staticmethod
    def extract_numbers(output: str) -> list[float]:
        """
        从输出中提取所有数字

        参数:
            output (str): API返回的输出字符串

        返回:
            list[float]: 提取的数字列表
        """
        return [float(num) for num in re.findall(r'\d+\.?\d*', output)]
    
    @staticmethod
    def clean_output(output: str) -> str:
        """
        清理输出，移除多余的空格和换行

        参数:
            output (str): API返回的输出字符串

        返回:
            str: 清理后的字符串
        """
        return ' '.join(output.strip().split())