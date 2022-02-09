import selectors
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse
from modules.models import HtmlItem as HtI


HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36', 'accept': '*/*'}
page_all_urls = []

# def get_html_with_JS(url):
#     session = HTMLSession()

#     # Use the object above to connect to needed webpage
#     resp = session.get(url)

#     # Run JavaScript code on webpage
#     resp.html.render()
#     r = resp.html.html
#     return  r

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def check_url_for_parse(soup, multipage, site_url):
    try:    # Check on the site link (with or without domain)
        get_html(soup.select(multipage)[-1].get('href'))
        site_url = soup.select(multipage)[-1].get('href')
        return site_url
    except:
        try:    # http + :// + domain + link
            site_url = urlparse(site_url).scheme + '://' + urlparse(
                site_url).netloc + soup.select(multipage)[-1].get('href')
            get_html(site_url)
            return site_url
        except:  # If the pages are graduated from:
            return ''


def get_items(items):
    ret_items = []
    for item in items:
        ret_items.append(HtI(
            item,                               # xml
            ' '.join(item.get_text().split()),  # text
            item.get('href'),
            item.get('id'),
            item.get('class'),
            item.get('src'),
            item.get('alt'),
            item.get('type'),
            item.get('name'),
            item.get('title'),
            item.get('style'))
        )
    return ret_items


def get_elements_from_page(html, selectors, multipage, site_url):
    ret = {
        "page": [],
        "next_page_url": ''
    }
    soup = BeautifulSoup(html.text, 'html.parser')
    if selectors == ['']:
        [str(tag) for tag in soup.find_all()]
        ret['page'] = get_items(soup.find_all())
        if multipage != '':
            ret['next_page_url'] = check_url_for_parse(
                soup, multipage, site_url)
        return ret
    for selector in selectors:
        ret_items = get_items(soup.select(selector))
        ret['page'] = ret_items
        if multipage != '':
            npu = check_url_for_parse(
                soup, multipage, site_url)
            if ret['next_page_url'] == npu: # checking on a repeating link
                return ret
            ret['next_page_url'] = npu
    return ret


def parser(site_url, selectors, multipage):
    pages = []
    while True:
        print("Parse page:\t", site_url)
        page_all_urls.append(site_url)
        page_html = get_html(site_url)
        page = get_elements_from_page(page_html, selectors, multipage, site_url)
        pages.append(tuple(page['page']))

        if multipage == '':
            return tuple(pages)
        if page['next_page_url'] == '':
            return tuple([page_all_urls, ([el for el in page] for page in pages)])
        site_url = page['next_page_url']

    """
        return format:
            [   # all pages
                [   # all elements on 1 page
                    HtmlItem( # class with any functions and __slots__:
                    '_xml', '_text', '_href', '_id', 
                    '_class', '_src', '_alt', '_type', 
                    '_name', '_title', '_style',
                    get_dict(), get_list(),
                    get_tuple(), get_json(),
                    get_csv(), get_xml(),
                    get_sql_insert()
                    ), 
                    HtmlItem, HtmlItem, ...
                ],
                [HtmlItem, HtmlItem, ...],
                [HtmlItem, HtmlItem, ...],
            ]
    """


def parser_tests():
    url = 'https://www.okidoki.ee/ru/buy/all/?query=%D0%BA%D0%BE%D0%BD%D1%81%D1%82%D1%80%D1%83%D0%BA%D1%82%D0%BE%D1%80&order=price'
    selectors = ['.pager__page']  # , '.subcategories']
    multipage = '.pager .pager__next'

    # url = 'https://themewagon.com/theme-price/free'
    # selectors = ['.page-item']
    # multipage = '.next.page-numbers.page-link'

    # url = 'https://kinogo-net.org/v68/'
    # selectors = ['.kino-item.ignore-select.kino-fix .kino-h']
    # multipage = '.pagi-nav.clearfix.ignore-select a'

    # url = 'http://scrumpoker.eu/oppeained/tarkvara-arendusprotsess/'
    # selectors = ['.menu-item.menu-item-type-post_type.menu-item-object-page a']
    # multipage = ''

    # url = 'https://bapehnkk.github.io/'
    # selectors = ['']
    # multipage = ''
    # When there are no selectors
    # structure ~~:
    # [
    #   [
    #       {'xml': '<html><head>...</head><body>...</body></html>', 'text': ...},
    #       {'xml': '<head>...</head><body>...</body>', 'text':...}, ...
    #   ],
    #   [ ... ], [ ... ], ...    #if multipage is not null
    # ]

    pages = parser(url, selectors, multipage)
    # print(pages)
    # Foreach for pages:
    # ==========================
    # for page in pages:
    #     for el in page:
    #         print(el.get_dict())
    # ==========================

