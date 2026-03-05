import functools
import sys


def log(filename=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__name__

            # Выбираем место для записи логов
            if filename:
                output = open(filename, 'a')
            else:
                output = sys.stdout

            try:
                result = func(*args, **kwargs)
                # Пишем результат в лог
                output.write(f"{func_name} ok\n")
                return result

            except Exception as e:
                # Пишем тип и входные данные ошибки
                error_type = type(e).__name__
                output.write(
                    f"{func_name} error: {error_type}. "
                    f"Inputs: {args}, {kwargs}\n"
                )
                raise  # Передаём ошибку дальше

            finally:  # Закрываем файл, если писали в него

                if filename:
                    output.close()

        return wrapper

    return decorator
