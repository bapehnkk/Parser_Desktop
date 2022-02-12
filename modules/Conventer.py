class Conventer:
    # __slots__ = ('__path', '__urls', ' __pages')
    def __init__(self, pages, path='exported_files/data.json'):
        self.__path = path
        self.__urls = pages[0]
        self.__pages = pages[-1]
        
        

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


    def export_to_json_file(self):
        import json
        pages = dict(zip(self.__urls, ([el.get_dict() for el in page] for page in self.__pages)))
        self.file_clear()
        with open(self.__path, 'w') as f:    
            json.dump(pages, f, indent=3)
            # for key, value in pages.items():
                # print(str(key)+'\n')
                # print(str([el for el in value])+'\n')

    def file_clear(self):
        with open(self.__path, "w", encoding="utf-8") as f:
            f.write('')