from urllib import request
import json

while 1:
    booklistpath = input("Input path to booklist:")
    try:
        f = open(booklistpath, "r")
        isbns = f.read()
        isbnlist = isbns.split('<br>')
        for isbn in isbnlist:
            try:
                w = request.urlopen("https://api.douban.com/v2/book/isbn/" + isbn)
                s = w.read()
                s = s.decode("utf-8")
                js = json.loads(s)
                print(js['alt'])
            except BaseException as e:
                print("Error occured when processing: " + isbn + "\n")
                print(e)
    except BaseException as e:
        print("Path to Booklist is invalid: " + e)
    finally:
        if f:
            f.close()
