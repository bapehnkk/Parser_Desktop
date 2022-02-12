import selectors
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from .models import Page, HtmlItem as HI


class Parser:

    HEADERS = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36', 'accept': '*/*'}

    def __init__(self, site_url, selectors=None, multipage=None, number_of_readable_pages=1000000):
        self.__site_url = site_url  # last site
        self.__selectors = selectors
        self.__multipage = multipage
        self.__req = self.__get_request(url=self.__site_url)
        self.__pages = []
        self.__error = ''
        self.__there_is_the_following_page = True
        self.__counter = number_of_readable_pages

        if self.__selectors == [''] or not isinstance(self.__selectors, list):
            self.__selectors = None
        if self.__selectors != None:
            for el in self.__selectors:
                if not isinstance(el, str):
                    self.__selectors = None
        if self.__multipage == '' or not isinstance(self.__multipage, str):
            self.__multipage = None

    def print_error(self):
        print(self.__error)
        return self.__error

    def parse(self):
        try:
            counter = 1
            while self.__there_is_the_following_page and counter < self.__counter:
                print(counter)
                self.__error = ''
                self.__there_is_the_following_page = False
                if self.__site_url == None:
                    self.__error = 'Site url is None (may be all\'re Ok)'
                    break

                if self.__req.status_code != 200:
                    self.__error = str(f'Exception: {self.__req}')
                    break
                # print('self.__site_url\t',self.__site_url)

                soup = BeautifulSoup(self.__req.text, 'html.parser')

                if self.__selectors == None:
                    self.__error = str('Exception: Slectors are not selected')
                    self.__pages.append(Page(url=self.__site_url, elements=[[
                        self.__create_HtmlItem(item=item) for item in soup.find_all()]  # foreach in soup items
                    ]))
                else:
                    self.__pages.append(Page(url=self.__site_url, elements=[
                        [self.__create_HtmlItem(item=item, s=selector) for item in soup.select(selector)    # foreach in soup items
                         ]for selector in self.__selectors                              # foreach in selectors
                    ]))

                if self.__multipage != None:
                    url_list = soup.select(self.__multipage)
                    if url_list != []:
                        # print(self.__site_url, soup.select(self.__multipage))
                        self.__check_url_for_next_page(
                            url_list[-1].get('href'))

                counter += 1
        except Exception as e:
            self.__error = e
            print(e)
        return self.__pages

    def __check_url_for_next_page(self, url):
        try:    # Check on the site link (with or without domain)
            check = self.__site_url
            self.__get_request(url)
            if check == self.__site_url:
                self.__there_is_the_following_page = True
        except:
            try:    # http + :// + domain + link
                check = self.__site_url
                site_url = self.__site_url
                site_url = urlparse(site_url).scheme + '://' + urlparse(
                    site_url).netloc + url
                self.__get_request(url=site_url)
                if check == self.__site_url:
                    self.__there_is_the_following_page = True
            except:  # If the pages are graduated from:
                self.__error = '''__check_url_for_next_page() return except (pages maybe they ended)'''

    def __create_HtmlItem(self, item, s=None):
        return HI(
            _selector=s,
            _xml=item,                                 # xml
            _text=' '.join(item.get_text().split()),   # text
            _href=item.get('href'),
            _id=item.get('id'),
            _class=item.get('class'),
            _src=item.get('src'),
            _alt=item.get('alt'),
            _type=item.get('type'),
            _name=item.get('name'),
            _title=item.get('title'),
            _style=item.get('style'))

    def __get_request(self, url, params=None):
        req = requests.get(
            url, headers=self.HEADERS, params=params)
        self.__req = req
        self.site_url =url
        return self.__req
        # print(self.__req)


def parser_test():
    #     url = 'https://www.okidoki.ee/ru/buy/all/?query=%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80&order=price'
    #     selectors = ['.pager__page']  # , '.subcategories']
    #     multipage = '.pager .pager__next'

    # url = 'https://themewagon.com/theme-price/free'
    # selectors = ['.page-item']
    # multipage = '.next.page-numbers.page-link'

    # url = 'https://kinogo-net.org/v68/'
    # url = 'http://scrumpoker.eu/oppeained/tarkvara-arendusprotsess/'
    # selectors = ['.menu-item.menu-item-type-post_type.menu-item-object-page a']
    # multipage = ''

    # url = 'https://bapehnkk.github.io/'
    # selectors = ['']
    # multipage = ''

    # p = Parser(url, selectors=selectors, multipage=multipage)
    # pages = p.parse()
    # p.print_error()
    # print(pages)

    # with open('./exported_files/data.txt', 'w', encoding="utf-8") as f:
    #     f.write(str(tuple([el.get_dict() for el in pages])))
    return


# parser_test()
