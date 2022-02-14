from encodings import utf_8


class Conventer:
    # __slots__ = ('__path', '__urls', ' __pages')
    def __init__(self, pages):
        self.__pages = pages
        self.__error = ''
    
    def save_to_csv_file(self):
        import pandas as pd  
        self.file_clear()
        
        pages = get_dict_f()
        df = pd.DataFrame(pages)
        
        # saving the dataframe 
        df.to_csv(self.__path) 

    def save_txt_file(self):
        self.file_clear()
        with open(self.__path, "a", encoding="utf-8") as f:
            pages = dict(zip(self.__urls, self.__pages))
            # print(pages)
            for key, value in pages.items():
                f.write(str(key)+'\n')
                f.write(str([el.get_dict() for el in value])+'\n')


    def export_to_json_file(self, path='exported_files/data.json'):
        import json
        self.file_clear(path)

        with open(path, 'w', encoding='utf_8') as f:    
            json.dump(tuple([el.get_dict() for el in self.__pages]), f, indent=3)
            # for key, value in pages.items():
                # print(str(key)+'\n')
                # print(str([el for el in value])+'\n')
        return self.__error

    def file_clear(self, path):
        with open(path, "w", encoding="utf-8") as f:
            f.write('')