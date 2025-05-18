# CogKit CodeRunner SDK

![CogKit Logo](https://coludai.cn/data_img/cogkit_Logo.svg)

CogKit CodeRunner SDK 是一个轻量级 Python 工具包，专为调用 SAI CodeRunner API（`https://coderunner.coludai.cn/api/run_code/python`）而设计。它简化了令牌生成、Python 代码执行和结果处理，支持同步运行单行或多行代码。

## CA 令牌申请

在使用 CogKit CodeRunner SDK 之前，您需要申请 CA 令牌。请联系 SAI 官方支持或访问以下链接获取申请流程：

[CA 令牌申请指南](https://coludai.cn/ca-application) <!-- 假设链接 -->

申请完成后，将您的 CA 令牌配置到项目的 `.env` 文件中，详见“安装指南”。

## 主要特性

- 简化 CodeRunner API 调用，运行 Python 代码
- 自动生成安全令牌（基于日期和代码的 MD5 加密）
- 支持单行和多行代码执行
- 智能解析 API 响应，获取执行结果
- 通过 `.env` 文件管理 CA 令牌

## 环境准备

- **Python 版本**：Python 3.8 或更高版本（已验证 Python 3.11）
- **操作系统**：Windows、Linux 或 macOS
- **网络**：确保可以访问 `https://coderunner.coludai.cn`

## 安装指南

1. 确保项目目录结构如下：

```
CogKit/
├── src/
│   ├── token_generator.py  # 令牌生成模块
│   ├── code_runner.py      # API 调用模块
├── tests/
│   ├── test_single_line.py # 测试单行代码
│   ├── test_multi_line.py  # 测试多行代码
│   ├── test_token.py       # 测试令牌生成
├── .env                    # CA 令牌配置文件
├── .env.example            # 配置文件模板
├── README.md               # 项目文档
├── requirements.txt        # 依赖列表
```

2. 安装依赖项：

```bash
cd CogKit
pip install -r requirements.txt
```

3. 配置 CA 令牌：

   - 复制 `.env.example` 到 `.env`：
     ```bash
     copy .env.example .env  # Windows
     cp .env.example .env    # Linux/Mac
     ```
   - 编辑 `.env` 文件，添加您的 CA 令牌：
     ```
     CA_TOKEN=your-ca-token-here
     ```
   - 将 `your-ca-token-here` 替换为实际的 CA 令牌（例如 `c9b3f395-f8e6-47f4-98c0-64b5ac6fc1f0`）
   - 如需申请令牌，请参考 [CA 令牌申请指南](https://coludai.cn/ca-application)

## 使用示例

### 1. 运行单行代码

执行单行 Python 代码并打印结果：

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.code_runner import CodeRunner

# 初始化 CodeRunner
runner = CodeRunner()
# 执行单行代码
result = runner.run_code("print('Hello SAI run!')")
# 打印结果
print("代码运行结果：", result.get("output", "无输出"))
```

### 2. 运行多行代码

执行多行 Python 代码并打印结果：

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.code_runner import CodeRunner

# 初始化 CodeRunner
runner = CodeRunner()
# 定义多行代码
code = """
def greet(name):
    return f"Hello, {name}!"
print(greet("SAI"))
print(greet("CogKit"))
"""
# 执行代码
result = runner.run_code(code)
# 打印结果
print("代码运行结果：", result.get("output", "无输出"))
```

### 3. 调试令牌生成

验证令牌生成逻辑：

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.token_generator import generate_token

# 生成令牌
code = "print('Hello SAI run!')"
token = generate_token(code)
print("生成令牌：", token)
```

## 运行测试

1. 进入项目目录：

```bash
cd CogKit
```

2. 运行测试脚本：

```bash
python -m unittest tests.test_single_line
python -m unittest tests.test_multi_line
python -m unittest tests.test_token
```

3. 查看运行结果：

   - 单行代码测试（`test_single_line.py`）输出：
     ```
     代码运行结果: Hello SAI run!
     ```
   - 多行代码测试（`test_multi_line.py`）输出：
     ```
     代码运行结果: Hello, SAI!
     Hello, CogKit!
     ```

## 常见问题解决

### 模块导入错误

如果遇到 `ModuleNotFoundError: No module named 'src'`：

- 确保在 CogKit 根目录下执行命令：
  ```bash
  cd CogKit
  python tests/test_single_line.py
  ```
- 或者使用 `unittest` 运行：
  ```bash
  python -m unittest tests.test_single_line
  ```
- 确认 `src/` 目录包含 `token_generator.py` 和 `code_runner.py`。

### API 调用失败（例如 403 Forbidden）

如果 API 调用失败：

- 检查 `.env` 文件中的 `CA_TOKEN` 是否正确：
  - 打开 `.env`，确保格式为：
    ```
    CA_TOKEN=your-actual-ca-token
    ```
  - 如果令牌无效，联系 SAI 官方支持申请新令牌。
- 运行以下调试脚本以查看详细响应：

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.code_runner import CodeRunner

runner = CodeRunner()
try:
    result = runner.run_code("print('Test')")
    print("响应：", result)
except Exception as e:
    print(f"错误：{e}")
```

保存为 `test_api.py`，然后运行：

```bash
python test_api.py
```

### 输出结果不可见

如果测试通过但未看到代码运行结果：

- 确保测试脚本包含打印语句，例如：
  ```python
  print("代码运行结果：", result.get("output", "无输出"))
  ```
- 检查 `tests/test_single_line.py` 是否为最新版本，包含输出逻辑。

### 清理缓存

如果遇到其他异常问题，尝试清理 Python 缓存：

```bash
# Windows
rmdir /S /Q src\__pycache__
rmdir /S /Q tests\__pycache__

# Linux/Mac
rm -rf src/__pycache__
rm -rf tests/__pycache__
```

## 依赖包

- requests==2.32.3
- python-dotenv==1.0.1

## 许可证

MIT