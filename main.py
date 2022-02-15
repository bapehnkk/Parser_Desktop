import eel, os
from modules.Parser import Parser as P
from modules.Conventer import Conventer as C

def eel_():
    eel.init('web')
    eel.start('main.html')
    
@eel.expose
def press_parse(url, selectors=None, multipage=None, path=None):
    errors = start_parse(url, selectors, multipage, path)
    eel.print_end(errors)

def start_parse(url, selectors=None, multipage=None, path=None):
    print(url, selectors, multipage)
    p = P(url, selectors=selectors, multipage=multipage)
    pages = p.parse()
    with open('web/exported_files/data.txt', 'w', encoding="utf-8") as f:
        f.write(str(pages))
    conv = C(pages)
    conv.export_to_json_file()

    return p.print_error(), conv.print_error()


def main():
    eel_()

if __name__ == '__main__':
    print('\r\nStart')
    print('_'*100)

    main()
    print('_'*100, '\r\nEND')
    