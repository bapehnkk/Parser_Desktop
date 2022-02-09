import eel
from modules.parser_with_slots import *
from modules.file_saver import FileExport as FE

def eel():
    eel.init('web')
    eel.start('main.html')



def main():
    url = 'https://www.okidoki.ee/ru/buy/all/?query=%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80&order=price'
    selectors = ['.pager__page']  # , '.subcategories']
    multipage = '.pager .pager__next'
    pages = parser(url, selectors, multipage)
    print(pages)
    FE(pages).export_to_json_file()

print('\r\nStart')
print('_'*100)

main()
print('_'*100, '\r\nEND')

# 