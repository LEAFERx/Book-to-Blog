# coding=utf-8

import json
import os
from datetime import datetime
from urllib import request

n = datetime.now()
if n.month < 10:
    nowtime = str(n.year) + ".0" + str(n.month)
else:
    nowtime = str(n.year) + "." + str(n.month)

while 1:
    booklistpath = input("Input path to booklist:")
    try:
        f = open(booklistpath, "r")
        result = []
        isbns = f.read()
        isbnlist = isbns.split('<br>')
        for isbn in isbnlist:
            try:
                w = request.urlopen(
                    "https://api.douban.com/v2/book/isbn/" + isbn)
                s = w.read()
                s = s.decode("utf-8")
                js = json.loads(s)
                if len(js['author']) > 1:
                    author = js['author'][0] + "等"
                else:
                    author = js['author'][0]
                result.append("- [" + nowtime + "  " + js['title'] + "  " +
                              author + "](" + js['alt'] + ")")
            except BaseException as e:
                print("Error occured when processing: " + isbn)
                print(e)
    except BaseException as e:
        print("Path to Booklist is invalid: " + e)
    finally:
        if f:
            f.close()
    try:
        fout = open(os.path.splitext(booklistpath)[0] + ".md", "wb")
        k = "\n".join(result)
        #print(k)
        fout.write(k.encode("utf-8"))
    except BaseException as e:
        print("Error occured when creating output file(" +
              os.path.splitext(booklistpath)[0] + ".md" + ")")
        print(e)
    finally:
        if fout:
            fout.close()
