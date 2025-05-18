# CogKit CodeRunner SDK

![CogKit Logo](https://coludai.cn/data_img/cogkit_Logo.svg)

The CogKit CodeRunner SDK is a lightweight Python toolkit designed for interacting with the SAI CodeRunner API (`https://coderunner.coludai.cn/api/run_code/python`). It simplifies token generation, Python code execution, and result handling, supporting synchronous execution of single-line or multi-line code.

## CA Token Application

Before using the CogKit CodeRunner SDK, you need to obtain a CA token. Please contact SAI official support or visit the following link for the application process:

[CA Token Application Guide](https://coludai.cn/ca-application) <!-- Assumed link -->

Once obtained, configure your CA token in the project's `.env` file, as detailed in the "Installation Guide".

## Key Features

- Simplified CodeRunner API calls for executing Python code
- Automatic generation of secure tokens (based on date and code MD5 hashing)
- Support for single-line and multi-line code execution
- Intelligent parsing of API responses to retrieve execution results
- CA token management via `.env` file

## Environment Setup

- **Python Version**: Python 3.8 or higher (tested with Python 3.11)
- **Operating System**: Windows, Linux, or macOS
- **Network**: Ensure access to `https://coderunner.coludai.cn`

## Installation Guide

1. Ensure the project directory structure is as follows:

```
CogKit/
├── src/
│   ├── token_generator.py  # Token generation module
│   ├── code_runner.py      # API call module
├── tests/
│   ├── test_single_line.py # Test single-line code
│   ├── test_multi_line.py  # Test multi-line code
│   ├── test_token.py       # Test token generation
├── .env                    # CA token configuration file
├── .env.example            # Configuration file template
├── README.md               # Project documentation
├── requirements.txt        # Dependency list
```

2. Install dependencies:

```bash
cd CogKit
pip install -r requirements.txt
```

3. Configure the CA token:

   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env  # Windows
     cp .env.example .env    # Linux/Mac
     ```
   - Edit the `.env` file to add your CA token:
     ```
     CA_TOKEN=your-ca-token-here
     ```
   - Replace `your-ca-token-here` with your actual CA token (e.g., `c9b3f395-f8e6-47f4-98c0-64b5ac6fc1f0`)
   - For token application, refer to the [CA Token Application Guide](https://coludai.cn/ca-application)

## Usage Examples

### 1. Running Single-Line Code

Execute a single line of Python code and print the result:

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.code_runner import CodeRunner

# Initialize CodeRunner
runner = CodeRunner()
# Execute single-line code
result = runner.run_code("print('Hello SAI run!')")
# Print result
print("Code execution result:", result.get("output", "No output"))
```

### 2. Running Multi-Line Code

Execute multi-line Python code and print the result:

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.code_runner import CodeRunner

# Initialize CodeRunner
runner = CodeRunner()
# Define multi-line code
code = """
def greet(name):
    return f"Hello, {name}!"
print(greet("SAI"))
print(greet("CogKit"))
"""
# Execute code
result = runner.run_code(code)
# Print result
print("Code execution result:", result.get("output", "No output"))
```

### 3. Debugging Token Generation

Verify the token generation logic:

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src.token_generator import generate_token

# Generate token
code = "print('Hello SAI run!')"
token = generate_token(code)
print("Generated token:", token)
```

## Running Tests

1. Navigate to the project directory:

```bash
cd CogKit
```

2. Run test scripts:

```bash
python -m unittest tests.test_single_line
python -m unittest tests.test_multi_line
python -m unittest tests.test_token
```

3. View execution results:

   - Single-line code test (`test_single_line.py`) output:
     ```
     Code execution result: Hello SAI run!
     ```
   - Multi-line code test (`test_multi_line.py`) output:
     ```
     Code execution result: Hello, SAI!
     Hello, CogKit!
     ```

## Troubleshooting

### Module Import Error

If you encounter `ModuleNotFoundError: No module named 'src'`:

- Ensure you run commands from the CogKit root directory:
  ```bash
  cd CogKit
  python tests/test_single_line.py
  ```
- Alternatively, use `unittest` to run:
  ```bash
  python -m unittest tests.test_single_line
  ```
- Verify that the `src/` directory contains `token_generator.py` and `code_runner.py`.

### API Call Failure (e.g., 403 Forbidden)

If an API call fails:

- Check if the `CA_TOKEN` in `.env` is correctly configured:
  - Open `.env` and ensure it follows:
    ```
    CA_TOKEN=your-actual-ca-token
    ```
  - If the token is invalid, contact SAI official support to obtain a new token.
- Run the following debug script to view detailed responses:

```python
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '.')))
from src.code_runner import CodeRunner

runner = CodeRunner()
try:
    result = runner.run_code("print('Test')")
    print("Response:", result)
except Exception as e:
    print(f"Error: {e}")
```

Save as `test_api.py` and run:

```bash
python test_api.py
```

### Missing Output

If tests pass but no code execution result is visible:

- Ensure test scripts include print statements, such as:
  ```python
  print("Code execution result:", result.get("output", "No output"))
  ```
- Verify that `tests/test_single_line.py` is the latest version with output logic.

### Clear Cache

If other issues arise, try clearing the Python cache:

```bash
# Windows
rmdir /S /Q src\__pycache__
rmdir /S /Q tests\__pycache__

# Linux/Mac
rm -rf src/__pycache__
rm -rf tests/__pycache__
```

## Dependencies

- requests==2.32.3
- python-dotenv==1.0.1

## License

MIT