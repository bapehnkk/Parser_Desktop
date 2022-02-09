import json
import pandas as pd
class HtmlItem:
    __slots__ = ('_xml', '_text', '_href', '_id', '_class',
                 '_src', '_alt', '_type', '_name', '_title', '_style')

    def __init__(self, _xml=None, _text=None, _href=None, _id=None, _class=None, _src=None, _alt=None, _type=None, _name=None, _title=None, _style=None):
        self._xml = str(_xml)
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
        return {slot: getattr(self, slot) for slot in self.__slots__}

    def get_list(self):
        return [self._xml, self._text, self._href, self._id, self._class, self._src, self._alt, self._type, self._name, self._title, self._style]

    def get_tuple(self):
        return self._xml, self._text, self._href, self._id, self._class, self._src, self._alt, self._type, self._name, self._title, self._style

    def get_json(self):
        return json.dumps(self.get_dict()) +','

    def get_csv(self, format='dict'):
        if format == 'list':
            return pd.DataFrame(self.get_list())
        elif format == 'tuple':
            return pd.DataFrame(self.get_tuple())
        else:
            try:
                return pd.DataFrame(self.get_dict())
            except:
                return pd.DataFrame(self.get_dict(), index=[0])
        
    def get_xml(self):
        return self._xml         

    def get_sql_insert(self, db_table_name):
        # placeholders = ', '.join(['%s'] * len(self.get_dict()))
        columns = ', '.join("`" + str(x).replace('/', '_') + "`" for x in self.get_dict().keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in self.get_dict().values())
        sql = "INSERT INTO %s ( %s ) VALUES ( %s );" % (db_table_name, columns, values)
        return sql
    


# Test
# item = HtmlItem(_xml='<a href="/">link</a>', _text='link', _href='/')
# # print(item._xml)

# el = item.get_dict()
# print("\r\nMy element\r\n")
# print(el)

