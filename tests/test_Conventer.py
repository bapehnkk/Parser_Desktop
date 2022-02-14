import pytest, sys, os
from difflib import SequenceMatcher
sys.path.append(os.getcwd())

def test_Conventer_сheck_for_similarity(): 
    from modules.Conventer import Conventer as C
    from modules.Parser import Parser as P

    C(P('https://www.google.com/').parse()).export_to_json_file()

    f1 = f2 = ''
    with open('exported_files/data.json', 'r', encoding='utf_8') as f:
        f1 = str(f.read())
    with open('tests/google_example.json', 'r', encoding='utf_8') as f:
        f2 = str(f.read())
    k = similar(f1, f2)

    assert k > 0.9

    
def test_Conventer_difference_checking(): 
    from modules.Conventer import Conventer as C
    from modules.Parser import Parser as P

    C(P('https://en.wikipedia.org/').parse()).export_to_json_file()

    f1 = f2 = ''
    with open('exported_files/data.json', 'r', encoding='utf_8') as f:
        f1 = str(f.read())
    with open('tests/google_example.json', 'r', encoding='utf_8') as f:
        f2 = str(f.read())
    k = similar(f1, f2)
    assert k < 0.8


def similar(a, b):
    return SequenceMatcher(None, a, b).quick_ratio()
if __name__ == '__main__':
    pytest.main()