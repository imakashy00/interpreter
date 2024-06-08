import contextlib
import io
import json


def execute_code(code):
    code = json.loads(code)
    python_code = code["code"]
    print("Executing Code!")
    local_vars = {}
    output = io.StringIO()
    try:
        with contextlib.redirect_stdout(output):
            exec(python_code, {}, local_vars)
    except Exception as e:
        return str(e)
    return output.getvalue()
