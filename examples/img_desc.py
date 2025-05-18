import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.cogkit import CogKit

def main():
    """示例：调用 SAI-img_desc API，描述图片内容"""
    # 初始化 CogKit
    cogkit = CogKit()
    
    # 提供图片 URL（请替换为实际可访问的图片 URL）
    image_url = "https://coludai.cn/data_img/hexagon-CFv8sjr3.svg"
    result = cogkit.img_desc(image_url)
    print("SAI-img_desc 图片描述：", result.get("output", "无输出"))

if __name__ == "__main__":
    main()