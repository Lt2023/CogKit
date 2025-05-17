from dotenv import load_dotenv
import os

def load_config() -> dict:
    """
    从环境变量加载配置

    返回:
        dict: 包含配置的字典，目前包括COGKIT_CA_TOKEN
    """
    load_dotenv()
    return {
        "COGKIT_CA_TOKEN": os.getenv("COGKIT_CA_TOKEN")
    }