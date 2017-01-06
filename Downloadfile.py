import requests
from bs4 import BeautifulSoup
import urllib2
import os
from sys import argv


def download(name,identifier):
    try:
        os.mkdir('hentai')
    except:
        pass
    try:
        #this is done so multiple instances of this script can be used simultaneously
        #unfinished download can't be finished so the folder must be deleted

        os.mkdir(('hentai/'+str(name)))
        for x in range(1, 1000):
            num = x
            try:
                g = 'https://i.nhentai.net/galleries/%r/%r.jpg' % (identifier, num)
                f = urllib2.urlopen(g)

            except Exception:
                try:
                    g = 'https://i.nhentai.net/galleries/%r/%r.png' % (identifier, num)
                    f = urllib2.urlopen(g)

                except Exception:
                    break
                    print("Done")
                    print

            data = f.read()

            text = name+" - "+str("%03d"%num)+".jpg"
            print str(text)
            text2 = 'hentai/' + name + '/' + text
            with open(text2, "wb") as code:
                code.write(data)

    except:
        print
        print("This manga is done")
        print
        print("Next")
        print
        pass


