import pytest, sys, os
sys.path.append(os.getcwd())


def test_HI_get_dict():
    from modules.models import HtmlItem as HI
    assert HI().get_dict() == {}
    assert HI(None, None, None, None, None, None, None,
              None, None, None, None, None).get_dict() == {}
    assert HI('#next-page',
              '<a id="next-page" href="some.site">Next page</a>', _id="next-page").get_dict() == {
        '_selector': '#next-page',
        '_xml': '<a id="next-page" href="some.site">Next page</a>',
        '_id': 'next-page'}
    assert HI(_selector='#next-page', _id="next-page").get_dict() == {
        '_selector': '#next-page',
        '_id': 'next-page'}

        
def test_HI_get_list():
    from modules.models import HtmlItem as HI
    assert HI().get_list() == [None,None,None,None,None,None,None,None,None,None,None,None]
    assert HI('#next-page', None, 'Next page', _id='next-page').get_list() == [
        '#next-page',None,'Next page',None,'next-page',None,None,None,None,None,None,None]

    
def test_HI_get_tuple():
    from modules.models import HtmlItem as HI
    assert HI().get_tuple() == (None,None,None,None,None,None,None,None,None,None,None,None)
    assert HI('#next-page', None, 'Next page', _id='next-page').get_tuple() == (
        '#next-page',None,'Next page',None,'next-page',None,None,None,None,None,None,None)

def test_HI_get_sql_insert():
    from modules.models import HtmlItem as HI
    assert HI().get_sql_insert('myTable') == '''INSERT INTO myTable (  ) VALUES (  );'''
    assert HI('#next-page',
              '<a id="next-page" href="some.site">Next page</a>', 
              _id="next-page").get_sql_insert('myTable') == '''INSERT INTO myTable ( `_selector`, `_xml`, `_id` ) VALUES ( '#next-page', '<a id="next-page" href="some.site">Next page<_a>', 'next-page' );'''



if __name__ == '__main__':
    pytest.main()
