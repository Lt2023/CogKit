from dotenv import load_dotenv
import os

def load_config():
    """加载环境配置
    
    Returns:
        dict: 包含 COGKIT_CA_TOKEN 的配置字典
    """
    load_dotenv()
    return {
        'COGKIT_CA_TOKEN': os.getenv('COGKIT_CA_TOKEN', '')
    }