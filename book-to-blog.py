from urllib import request
import json

while 1:
    isbn = input()
    try:
        f = request.urlopen("https://api.douban.com/v2/book/isbn/" + isbn)
        s = f.read()
        s = s.decode("utf-8")
        js = json.loads(s)
        print(js['code'])
    except Exception as e:
        print(e)
        
    
