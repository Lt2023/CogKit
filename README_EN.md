# CogKit SDK

![CogKit Logo](https://raw.githubusercontent.com/Lt2023/CogKit/155e3802ade3557eb8a5f80f582abc310b5361fe/src/img/cogkit_Logo.svg)

CogKit SDK is a convenient Python toolkit designed for calling CogKit's `/api/run_code/python` interface. It simplifies the entire process of remotely executing Python code, supporting synchronous and asynchronous calls, batch code execution, and intelligent result parsing.

## CA Token Application

Before using the CogKit SDK, you need to apply for a CA token. For detailed application process and instructions, please refer to the following document:

[CA Token Application Guide](https://www.yuque.com/liushiancoludai/oei1as/xl9qnfphp2e26p0a)

After completing the application according to the guide, please configure the obtained CA token in the project's `.env` file.

## Main Features

- Easily run Python code and obtain execution results
- Intelligently generate security tokens required by the API
- Flexibly support batch execution of multiple code segments
- Efficient asynchronous call mode, perfectly suitable for high concurrency scenarios
- Intelligent parsing of output results (e.g., automatic extraction of numerical data)

## Installation Guide

1. First, ensure your project directory structure is as follows:
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

2. Install the required dependencies:
```bash
cd CogKit
pip install -r requirements.txt
```

3. Configure your CA token:
   - Create or edit the `.env` file in the project root directory
   - Add your CA token configuration:
   ```
   COGKIT_CA_TOKEN=your-ca-token-here
   ```
   - Please replace `your-ca-token-here` with your actual CA token value
   - If you don't have a CA token yet, please refer to the [CA Token Application Guide](https://www.yuque.com/liushiancoludai/oei1as/xl9qnfphp2e26p0a) to apply

## Usage Examples

### 1. Basic Call

Below is a simple example of running a single Python code snippet:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.client import CogKitRunner

# Create runner instance
runner = CogKitRunner()
# Define code to execute
code = "print('Hello CogKit!')"
# Execute code and get results
result = runner.run_code(code)
# Output results
print("Output:", result.get("output"))
print("Execution status:", result.get("success"))
```

### 2. Batch Execution

Need to execute multiple code segments? This example demonstrates the convenient way of batch execution:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.client import CogKitRunner

# Create runner instance
runner = CogKitRunner()
# Define multiple code segments
codes = [
    "print('Task 1')", 
    "print('Task 2')", 
    "for i in range(3): print(i)"
]
# Execute in batch and get results
results = runner.run_code_batch(codes)
# Output execution results for each code segment
for i, result in enumerate(results):
    print(f"Code {i+1} execution result: {result}")
```

### 3. Asynchronous Call

For scenarios requiring non-blocking execution, asynchronous call mode is very useful:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import asyncio
from src.client import CogKitRunner

async def main():
    # Create runner instance
    runner = CogKitRunner()
    # Define code to execute
    code = "print('Async CogKit run!')"
    # Execute code asynchronously
    result = await runner.run_code_async(code)
    # Output results
    print("Output:", result.get("output"))
    print("Execution status:", result.get("success"))

# Run async main function
asyncio.run(main())
```

## Execution Steps

1. Open command prompt, navigate to the project directory:
```bash
cd CogKit
```

2. Run example scripts:
```bash
python examples/basic.py
python examples/batch.py
python examples/async.py
```

## Common Issues and Solutions

### Module Import Error
If you encounter `ModuleNotFoundError: No module named 'src'`:
- Make sure you are in the CogKit root directory when executing commands
```bash
cd CogKit
python examples/basic.py
```

### API Call Failure
If the API call fails:
- Check if the `COGKIT_CA_TOKEN` in the `.env` file is correctly configured
- Run the following test script to view detailed API response:

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
    print(f"Error: {e}")
```

Save as `test_api.py`, then run:
```bash
python test_api.py
```

### Clearing Cache
If you encounter other exceptional issues, try clearing the Python cache:
```bash
# Windows
rmdir /S /Q src\__pycache__
rmdir /S /Q examples\__pycache__

# Linux/Mac
rm -rf src/__pycache__
rm -rf examples/__pycache__
```

## Dependencies

- requests==2.32.3
- aiohttp==3.10.5
- python-dotenv==1.0.1

## License

MIT
