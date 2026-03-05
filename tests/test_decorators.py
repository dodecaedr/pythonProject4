import os
import pytest

from src.decorators import log


# Вспомогательная функция для очистки тестового файла
def cleanup_test_file(filename):
    if os.path.exists(filename):
        os.remove(filename)


class TestLogDecorator:
    """Тесты для декоратора log."""

    def test_success_with_filename(self):
        """Тест: успешное выполнение функции с записью в файл."""
        test_file = "test_log.txt"
        cleanup_test_file(test_file)

        @log(filename=test_file)
        def test_func(a, b):
            return a + b

        result = test_func(2, 3)
        assert result == 5

        # Проверяем содержимое файла
        with open(test_file, 'r') as f:
            content = f.read().strip()
        assert content == "test_func ok"

        cleanup_test_file(test_file)

    def test_error_with_filename(self):
        """Тест: ошибка в функции с записью в файл."""
        test_file = "test_log.txt"
        cleanup_test_file(test_file)

        @log(filename=test_file)
        def problematic_func(x):
            if x < 0:
                raise ValueError("Negative value")
            return x ** 0.5

        with pytest.raises(ValueError, match="Negative value"):
            problematic_func(-1)

        # Проверяем содержимое файла
        with open(test_file, 'r') as f:
            content = f.read().strip()
        expected = "problematic_func error: ValueError. Inputs: (-1,), {}"
        assert content == expected

        cleanup_test_file(test_file)

    def test_success_to_console(self, capsys):
        """Тест: успешное выполнение с выводом в консоль."""

        @log()
        def simple_func():
            return "hello"

        result = simple_func()
        assert result == "hello"

        # Перехватываем вывод в консоль
        captured = capsys.readouterr()
        assert captured.out.strip() == "simple_func ok"

    def test_error_to_console(self, capsys):
        """Тест: ошибка с выводом в консоль."""

        @log()
        def error_func():
            raise TypeError("Something went wrong")

        with pytest.raises(TypeError, match="Something went wrong"):
            error_func()

        # Перехватываем вывод в консоль
        captured = capsys.readouterr()
        expected = "error_func error: TypeError. Inputs: (), {}"
        assert captured.out.strip() == expected

    def test_function_with_args_and_kwargs(self, capsys):
        """Тест: функция с позиционными и ключевыми аргументами."""

        @log()
        def complex_func(a, b, c=0, d=1):
            return (a + b) * (c + d)

        result = complex_func(2, 3, c=4, d=5)
        assert result == 45

        captured = capsys.readouterr()
        expected = "complex_func ok"
        assert captured.out.strip() == expected

    def test_multiple_calls(self):
        """Тест: несколько вызовов функции с записью в один файл."""
        test_file = "multiple_calls.txt"
        cleanup_test_file(test_file)

        @log(filename=test_file)
        def counter(x):
            return x + 1

        counter(1)
        counter(2)
        counter(3)

        # Проверяем, что все вызовы записаны
        with open(test_file, 'r') as f:
            lines = f.readlines()

        assert len(lines) == 3
        assert all("counter ok" in line for line in lines)

        cleanup_test_file(test_file)

    def test_exception_preservation(self):
        """Тест: исключение передаётся дальше после логирования."""

        @log(filename="exception_test.txt")
        def risky_func():
            raise RuntimeError("Critical error")

        with pytest.raises(RuntimeError, match="Critical error"):
            risky_func()

        # Проверяем логирование ошибки
        with open("exception_test.txt", 'r') as f:
            content = f.read().strip()
        expected = "risky_func error: RuntimeError. Inputs: (), {}"
        assert content == expected

        cleanup_test_file("exception_test.txt")
