import time
import sys
import json


class HtmlItem:
    __slots__ = ('i_xml', 'i_text', 'i_href', 'i_id', 'i_class',
                 'i_src', 'i_alt', 'i_type', 'i_name', 'i_title', 'i_style')

    def __init__(self, i_xml=None, i_text=None, i_href=None, i_id=None, i_class=None, i_src=None, i_alt=None, i_type=None, i_name=None, i_title=None, i_style=None):
        self.i_xml = i_xml
        self.i_text = i_text
        self.i_href = i_href
        self.i_id = i_id
        self.i_class = i_class
        self.i_src = i_src
        self.i_alt = i_alt
        self.i_type = i_type
        self.i_name = i_name
        self.i_title = i_title
        self.i_style = i_style

    

item = HtmlItem(i_xml='<a href="/">link</a>', i_text='link', i_href='/')
print(item.i_xml)
cs = sys.getsizeof(item)

dict = {
    'xml': '<a href="/">link</a>',
    'text': 'link',
    'href': '/',
    'id': None,
    'class': None,
    'src': None,
    'alt': None,
    'type': None,
    'name': None,
    'title': None,
    'style': None
}
ds = sys.getsizeof(dict)

print("\r\nSize:\t", cs, ds)


# ======================================================================================================================

# ======================================================================================================================

# ======================================================================================================================

def print_dict():
    for i in range(100000):
        print(dict['xml'],
              dict['text'],
              dict['href'],
              dict['id'],
              dict['class'],
              dict['src'],
              dict['alt'],
              dict['type'],
              dict['name'],
              dict['title'],
              dict['style']
              )
              
    # --- 33.60037088394165 seconds dict ---
    # --- 35.09343075752258 seconds dict ---



def print_slots():
    for i in range(100000):
        print(item.i_xml, item.i_text, item.i_href, item.i_id, item.i_class,
              item.i_src, item.i_alt, item.i_type, item.i_name, item.i_title, item.i_style)
    # --- 33.674487590789795 seconds slots ---
    # --- 35.794071197509766 seconds slots ---


def append_dict():# not actual
    some_list = []
    for i in range(10000000):
        some_list.append(dict)
    some_list = tuple(some_list)
    # --- 1.1851792335510254 seconds ---
    # --- 1.1698739528656006 seconds ---
    # --- 1.150177001953125 seconds ---
    # --- 1.151137351989746 seconds ---
    # --- 1.154381275177002 seconds ---
    # --- 1.153071403503418 seconds ---
    # --- 1.1579351425170898 seconds ---
    # --- 1.1509227752685547 seconds ---
    # --- 1.1598091125488281 seconds ---
    # --- 1.1529459953308105 seconds ---
    # ====================================================================================================
    # Averageе:        1.15854332447052


def append_slots():# not actual
    some_list = []
    for i in range(10000000):
        some_list.append(item)
    some_list = tuple(some_list)
        # --- 1.1620633602142334 seconds ---
        # --- 1.1319990158081055 seconds ---
        # --- 1.1329302787780762 seconds ---
        # --- 1.1299784183502197 seconds ---
        # --- 1.1240143775939941 seconds ---
        # --- 1.1260929107666016 seconds ---
        # --- 1.1391608715057373 seconds ---
        # --- 1.148033618927002 seconds ---
        # --- 1.1342289447784424 seconds ---
        # --- 1.1344101428985596 seconds ---
        # ====================================================================================================
        # Averageе:        1.1362911939620972

# ======================================================================================================================

# ======================================================================================================================

# ======================================================================================================================


def to_json_dict():
    pages = []
    for i in range(100):
        page = []
        for element in range(1000000):
            page.append(item.toJSON())
        pages.append(tuple(page))
    pages = json.dumps(tuple(pages))

    with open('data.json', "w", encoding="utf-8") as f:
        f.write(pages)



averageе = 0

for i in range(10):
    start_time = time.time()
    to_json_dict()
    averageе += time.time() - start_time
    print("--- %s seconds ---" % (time.time() - start_time))

print("="*100)
print("Averageе:\t", averageе/10)

# win __slots__
# For versatility