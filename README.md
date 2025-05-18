# CogKit SDK

![CogKit Logo](./src/img/cogkit_logo.svg)

CogKit SDK 是一个便捷的 Python 工具包，专为调用 SAI API（包括 SAI-Chat-L6、SAI-Reasoner3mini、SAI-img_desc、SAI-tts、SAI-txt2img、SAI-Coder 和 CodeRunner）而设计。它简化了令牌生成、API 调用和结果处理，支持同步、异步和批量操作，以及智能响应解析。

## CA 令牌申请

在使用 CogKit SDK 之前，您需要申请 CA 令牌。请参考以下官方指南获取详细申请流程：

CA 令牌申请指南

申请完成后，将您的 CA 令牌配置到项目的 `.env` 文件中。

## 主要特性

- 简化的 SAI API 端点访问
- 自动生成安全的 API 令牌
- 支持同步、异步和批量 API 请求
- 智能解析 API 响应
- 可配置的会话管理以支持对话历史

## 安装指南

1. 确保项目目录结构如下：

```
CogKit/
├── src/
│   ├── __init__.py
│   ├── cogkit.py
│   ├── token.py
│   ├── config.py
│   ├── img/
│   │   ├── cogkit_logo.svg
├── examples/
│   ├── basic.py
│   ├── batch.py
│   ├── async.py
├── README.md
├── .env
├── .env.example
├── requirements.txt
```

2. 安装依赖项：

```bash
cd CogKit
pip install -r requirements.txt
```

3. 配置 CA 令牌：

   - 复制 `.env.example` 到 `.env`
   - 编辑 `.env` 文件，添加您的 CA 令牌：

   ```
   COGKIT_CA_TOKEN=your-ca-token-here
   ```

   - 将 `your-ca-token-here` 替换为实际的 CA 令牌
   - 如需申请令牌，请参考 CA 令牌申请指南

## 使用示例

### 1. 基本 API 调用（SAI-Chat-L6）

运行单个聊天查询：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cogkit import CogKit

# 初始化 CogKit
cogkit = CogKit()
# 执行聊天请求
result = cogkit.chat_l6(prompt="你是谁？")
print("响应：", result.get("output"))
```

### 2. 批量 API 调用（SAI-Coder）

执行多个代码相关查询：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.cogkit import CogKit

# 初始化 CogKit
cogkit = CogKit()
# 定义多个提示
prompts = [
    "编写一个计算阶乘的 Python 函数",
    "解释 Python 中的冒泡排序",
    "创建一个简单的 Python 类"
]
# 批量执行
results = cogkit.coder_batch(prompts)
# 输出结果
for i, result in enumerate(results):
    print(f"结果 {i+1}：{result}")
```

### 3. 异步 API 调用（SAI-tts）

异步生成文本转语音：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import asyncio
from src.cogkit import CogKit

async def main():
    # 初始化 CogKit
    cogkit = CogKit()
    # 异步生成语音
    result = await cogkit.tts_async("你好，这是 CogKit！")
    print("音频 URL：", f"https://ai.coludai.cn{result.get('dir')}")
    print("状态：", result.get("status"))

asyncio.run(main())
```

## 运行示例

1. 进入项目目录：

```bash
cd CogKit
```

2. 运行示例脚本：

```bash
python examples/basic.py
python examples/batch.py
python examples/async.py
```

## 常见问题解决

### 模块导入错误

如果遇到 `ModuleNotFoundError: No module named 'src'`：

- 确保您在 CogKit 根目录下执行命令：

```bash
cd CogKit
python examples/basic.py
```

### API 调用失败

如果 API 调用失败：

- 检查 `.env` 文件中的 `COGKIT_CA_TOKEN` 是否正确配置
- 运行以下测试脚本以查看详细的 API 响应：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.cogkit import CogKit

cogkit = CogKit()
try:
    result = cogkit.chat_l6("测试查询")
    print(result)
except Exception as e:
    print(f"错误：{e}")
```

保存为 `test_api.py`，然后运行：

```bash
python test_api.py
```

### 清理缓存

如果遇到其他异常问题，尝试清理 Python 缓存：

```bash
# Windows
rmdir /S /Q src\__pycache__
rmdir /S /Q examples\__pycache__

# Linux/Mac
rm -rf src/__pycache__
rm -rf examples/__pycache__
```

## 依赖包

- requests==2.32.3
- aiohttp==3.10.5
- python-dotenv==1.0.1

## 许可证

MIT