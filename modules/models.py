import requests


class HtmlItem:
    __slots__ = ('_selector', '_xml', '_text', '_href', '_id', '_class',
                 '_src', '_alt', '_type', '_name', '_title', '_style')

    def __init__(self, _selector=None, _xml=None, _text=None, _href=None, _id=None, _class=None, _src=None, _alt=None, _type=None, _name=None, _title=None, _style=None):
        self._selector = _selector
        self._xml = _xml if _xml == None else str(_xml)
        self._text = _text
        self._href = _href
        self._id = _id
        self._class = _class
        self._src = _src
        self._alt = _alt
        self._type = _type
        self._name = _name
        self._title = _title
        self._style = _style

    def get_dict(self):
        return {slot: getattr(self, slot) for slot in self.__slots__ if getattr(self, slot) != None}

    def get_list(self):
        return [self._selector, self._xml, self._text, self._href, self._id, self._class, self._src, self._alt, self._type, self._name, self._title, self._style]

    def get_tuple(self):
        return self._selector, self._xml, self._text, self._href, self._id, self._class, self._src, self._alt, self._type, self._name, self._title, self._style

    # def get_json(self):
    #     return json.dumps(self.get_dict()) + ','

    # def get_csv(self, format='dict'):
    #     if format == 'list':
    #         return pd.DataFrame(self.get_list())
    #     elif format == 'tuple':
    #         return pd.DataFrame(self.get_tuple())
    #     else:
    #         try:
    #             return pd.DataFrame(self.get_dict())
    #         except:
    #             return pd.DataFrame(self.get_dict(), index=[0])

    # def get_xml_text(self):
    #     return self._xml

    def get_sql_insert(self, db_table_name):
        # placeholders = ', '.join(['%s'] * len(self.get_dict()))
        columns = ', '.join("`" + str(x).replace('/', '_') +
                            "`" for x in self.get_dict().keys())
        values = ', '.join("'" + str(x).replace('/', '_') +
                           "'" for x in self.get_dict().values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (
            db_table_name, columns, values)
        return sql


# Test
# item = HtmlItem(_xml='<a href="/">link</a>', _text='link', _href='/')
# # print(item._xml)

# el = item.get_dict()
# print("\r\nMy element\r\n")
# print(el)

class Page:
    __slots__ = ('_Page__error', '_Page__url', '_Page__elements')
    def __init__(self, url, elements):
        self.__error = ''
        self.__url = ''
        self.__elements = tuple([])
        if isinstance(url, (str)):
            if self.check_site(url):
                self.__url = url
            else:
                self.__error = 'This site does not open'
        else:
            self.__error = 'url is not string'
        # Creating and sorting empty lists
        try:
            self.__elements = list(filter(None, elements))
            self.__elements = tuple([[j.get_dict() for j in i] for i in self.__elements])
        except:
            self.__error = 'Incorrect data type (elements!=[[HtmlItem,...],...])'

        
    def print_error(self):
        print(self.__error)
        return self.__error

    def get_dict(self):
        # print([[j.get_dict() for j in i] for i in self.__elements])
        return {
            'url': self.__url,
            'elements': self.__elements, 
            'error': self.__error
        }

    def check_site(self, site_name):
        try:
            requests.get(site_name)
            return True
        except:
            self.__error = 'Unknown site'
            return False

