import eel
from modules.Parser import Parser as P


def eel_():
    eel.init('web')
    eel.start('main.html')

@eel.expose
def my_python_function(url, selectors=None, multipage=None):
    print(url, selectors, multipage)
    p = P(url, selectors=selectors, multipage=multipage)
    pages = p.parse()
    p.print_error()
    print(pages)

def main():
    eel_()
    url = 'https://www.okidoki.ee/ru/buy/all/?query=%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80&order=price'
    selectors = ['.pager__page']  # , '.subcategories']
    multipage = '#category-big-list > div.pager > div.pager__center > ul > li:nth-child(4) > a'



print('\r\nStart')
print('_'*100)

main()
print('_'*100, '\r\nEND')

#
