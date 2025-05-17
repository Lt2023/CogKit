# CogKit SDK

![CogKit Logo](https://raw.githubusercontent.com/Lt2023/CogKit/155e3802ade3557eb8a5f80f582abc310b5361fe/src/img/cogkit_Logo.svg)

CogKit SDK 是一个便捷的 Python 工具包，专为调用 CogKit 的 `/api/run_code/python` 接口而设计。它简化了远程执行 Python 代码的整个流程，支持同步和异步调用方式、批量代码执行以及结果智能解析等实用功能。

## CA 令牌申请

在使用 CogKit SDK 之前，你需要申请 CA 令牌。详细的申请流程和说明请参考以下文档：

[CA 令牌申请指南](https://www.yuque.com/liushiancoludai/oei1as/xl9qnfphp2e26p0a)

请按照指南完成申请后，将获得的 CA 令牌配置到项目的 `.env` 文件中。

## 主要特性

- 轻松运行 Python 代码并获取执行结果
- 智能自动生成 API 所需的安全令牌
- 灵活支持多段代码的批量执行
- 高效异步调用模式，完美适配高并发场景
- 智能解析输出结果（例如自动提取数值数据）

## 安装指南

1. 首先确保你的项目目录结构如下：
```
CogKit/
├── src/
│   ├── __init__.py
│   ├── client.py
│   ├── token.py
│   ├── config.py
│   ├── parser.py
├── examples/
│   ├── basic.py
│   ├── batch.py
│   ├── async.py
├── README.md
├── .env
├── requirements.txt
```

2. 安装所需依赖：
```bash
cd CogKit
pip install -r requirements.txt
```

3. 配置你的 CA 令牌：
   - 创建或编辑项目根目录下的 `.env` 文件
   - 添加你的 CA 令牌配置：
   ```
   COGKIT_CA_TOKEN=your-ca-token-here
   ```
   - 请将 `your-ca-token-here` 替换为你的实际 CA 令牌值
   - 如果你还没有 CA 令牌，请参考[CA令牌申请指南](https://www.yuque.com/liushiancoludai/oei1as/xl9qnfphp2e26p0a)进行申请

## 使用示例

### 1. 基本调用

下面是运行单个 Python 代码片段的简单示例：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.client import CogKitRunner

# 创建运行器实例
runner = CogKitRunner()
# 定义要执行的代码
code = "print('Hello CogKit!')"
# 执行代码并获取结果
result = runner.run_code(code)
# 输出结果
print("输出:", result.get("output"))
print("执行状态:", result.get("success"))
```

### 2. 批量执行

需要执行多段代码？这个示例展示了批量执行的便捷方式：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.client import CogKitRunner

# 创建运行器实例
runner = CogKitRunner()
# 定义多段代码
codes = [
    "print('Task 1')", 
    "print('Task 2')", 
    "for i in range(3): print(i)"
]
# 批量执行并获取结果
results = runner.run_code_batch(codes)
# 输出每段代码的执行结果
for i, result in enumerate(results):
    print(f"代码 {i+1} 执行结果: {result}")
```

### 3. 异步调用

对于需要非阻塞执行的场景，异步调用模式非常有用：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import asyncio
from src.client import CogKitRunner

async def main():
    # 创建运行器实例
    runner = CogKitRunner()
    # 定义要执行的代码
    code = "print('Async CogKit run!')"
    # 异步执行代码
    result = await runner.run_code_async(code)
    # 输出结果
    print("输出:", result.get("output"))
    print("执行状态:", result.get("success"))

# 运行异步主函数
asyncio.run(main())
```

## 运行步骤

1. 打开命令提示符，进入项目目录：
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
- 确保你在执行命令时位于 CogKit 根目录下
```bash
cd CogKit
python examples/basic.py
```

### API 调用失败
如果 API 调用失败：
- 检查 `.env` 文件中的 `COGKIT_CA_TOKEN` 是否正确配置
- 运行以下测试脚本查看详细的 API 响应：

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.client import CogKitRunner

runner = CogKitRunner()
try:
    result = runner.run_code("print('Test')")
    print(result)
except Exception as e:
    print(f"错误: {e}")
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
