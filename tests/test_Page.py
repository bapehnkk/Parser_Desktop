import pytest
import sys
import os
sys.path.append(os.getcwd())


def test_P_returns_empty_dictionary():
    from modules.models import Page as P
    assert P('some.site.com', []).get_dict() == {
        'elements': (), 'url': '', 'error': 'This site does not open'}
    assert P('some.site.com', ()).get_dict() == {
        'elements': (), 'url': '', 'error': 'This site does not open'}
    assert P('', []).get_dict() == {'elements': (), 'url': '', 'error': 'This site does not open'}
    assert P([], '').get_dict() == {'elements': (), 'url': '', 'error': 'url is not string'}
    assert P('', []).get_dict() == {'elements': (), 'url': '', 'error': 'This site does not open'}


def test_P_returns_dict():
    from modules.models import Page as P
    from modules.models import HtmlItem as HI
    item = HI(_selector='#next-page', _id="next-page")
    assert P('https://www.google.com/', [[item, item]]).get_dict() == {
        'url': 'https://www.google.com/',
        'elements': ([{'_id': 'next-page', '_selector': '#next-page'},
                      {'_id': 'next-page', '_selector': '#next-page'}],),
        'error': ''}
    assert P('https://www.google.com/', [[]]).print_error() == ''
    assert P('https://www.google.com/', [[[], item]]).print_error(
    ) == 'Incorrect data type (elements!=[[HtmlItem,...],...])'


if __name__ == '__main__':
    pytest.main()
