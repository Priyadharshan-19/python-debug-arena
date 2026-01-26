import sys
import subprocess
from utils.security import validate_code_safety

def execute_python_code(user_code):
    # 🛡️ Step 1: Safety Scan (block dangerous code)
    is_safe, error_msg = validate_code_safety(user_code)
    if not is_safe:
        return {"status": "error", "output": error_msg}

    # 🚀 Step 2: Execute code with strict limits
    try:
        process = subprocess.run(
            [sys.executable, "-c", user_code],
            capture_output=True,
            text=True,
            timeout=2,          # ⏱️ Hard limit: 2 seconds
            shell=False         # 🔒 Prevent shell injection
        )

        stdout = process.stdout.strip()
        stderr = process.stderr.strip()

        if stderr:
            return {"status": "error", "output": stderr}

        return {"status": "success", "output": stdout}

    except subprocess.TimeoutExpired:
        return {
            "status": "error",
            "output": "Time Limit Exceeded (Possible infinite loop)"
        }
    except Exception as e:
        return {"status": "error", "output": str(e)}
