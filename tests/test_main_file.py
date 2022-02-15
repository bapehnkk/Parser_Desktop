import pytest, sys, os
sys.path.append(os.getcwd())
from main import start_parse

def test_error_is_None():
    error = start_parse('https://www.google.com/', ['body'])
    assert error == ('', '')

def test_ret_error():
    error = start_parse('https://www.google.com/', )
    assert error != ('', '')

if __name__ == '__main__':
    pytest.main()
