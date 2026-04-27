import functools
import sys
from typing import Callable, Any, Union, TextIO


def log(filename: Union[str, None] = None) -> Callable:
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            func_name = func.__name__

            if filename:
                output: TextIO = open(filename, "a", encoding="utf-8")
            else:
                output = sys.stdout

            try:
                result = func(*args, **kwargs)
                output.write(f"{func_name} ok\n")
                return result
            except Exception as e:
                error_type = type(e).__name__
                output.write(f"{func_name} error: {error_type}. " f"Inputs: {args}, {kwargs}\n")
                raise
            finally:
                if filename and output is not sys.stdout:
                    output.close()

        return wrapper

    return decorator
