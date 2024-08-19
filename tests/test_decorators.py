import pytest

from src.decorators import log


def test_log1():
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y
    result = my_function(2, 2)

    assert result == 4

def test_log2(capsys):
    @log(filename="test_log.txt")
    def my_function(x, y):
        return x + y
    # Проверка ошибки
    try:
        my_function()
    except TypeError:
        captured = capsys.readouterr()
        assert "my function error: " in captured.out