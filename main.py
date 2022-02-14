import eel
from modules.Parser import Parser as P
from modules.Conventer import Conventer as C

def eel_():
    eel.init('web')
    eel.start('main.html')
    
@eel.expose
def my_python_function(url, selectors=None, multipage=None):
    print(url, selectors, multipage)
    p = P(url, selectors=selectors, multipage=multipage)
    pages = p.parse()
    p.print_error()
    
    with open('exported_files/data.txt', 'w', encoding="utf-8") as f:
        f.write(str(tuple([el.get_dict() for el in pages])))

    C(pages).export_to_json_file()

def main():
    eel_()

if __name__ == '__main__':
    print('\r\nStart')
    print('_'*100)

    main()
    print('_'*100, '\r\nEND')
    