from urllib import request
import json
import os

while 1:
    booklistpath = input("Input path to booklist:")
    try:
        f = open(booklistpath, "r")
        result = []
        isbns = f.read()
        isbnlist = isbns.split('<br>')
        for isbn in isbnlist:
            try:
                w = request.urlopen("https://api.douban.com/v2/book/isbn/" + isbn)
                s = w.read()
                s = s.decode("utf-8")
                js = json.loads(s)
                author = js['author'].length() > 1 ? js['author'][0] + "等" : js['author'][0]
                result.push("!["+ js['title'] + " "+ js['author'] + "](" + js['alt'] + ")")
            except BaseException as e:
                print("Error occured when processing: " + isbn + "\n")
                print(e)
    except BaseException as e:
        print("Path to Booklist is invalid: " + e)
    finally:
        if f:
            f.close()
    try:
        fout = open(os.path.splitext(booklistpath)[0] + ".md", "w")
        k = result.join("\n")
        fout.write(k)
    except BaseException as e:
        print("Error occured when creating output file(" + os.path.splitext(booklistpath)[0] + ".md" + ")" + ":" + e)
    finally:
        if fout:
            fout.close
