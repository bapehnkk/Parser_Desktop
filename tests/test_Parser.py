import pytest
import sys
import os
sys.path.append(os.getcwd())


def test_Parser_ret():
    from modules.models import Page as P
    from modules.Parser import Parser as Par
    
    url = 'https://www.google.com/'

    assert isinstance(Par(url).parse()[0], P)
    assert isinstance(Par('not url').parse(), (tuple))


if __name__ == '__main__':
    pytest.main()
