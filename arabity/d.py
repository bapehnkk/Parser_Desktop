def dic():
    d = {}



{
    "text":     "some text",
    "id":       "some id",
    "class":    "some class",
    "href":     "some url"
}

# входные данные
['text', 'href']

# ожидаемый результат
{
    "text":     "some text",
    "id":       "",
    "class":    "",
    "href":     "some url"
}



from urllib.parse import urlparse
address = urlparse("http://sub.sub.domain.tld/as/fa")

print(address.netloc)
print(address.path)
print(address.scheme)

