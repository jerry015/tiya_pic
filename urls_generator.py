import cookielib
import urllib2
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
import requests

def urls_gen(purl):
    urls = []
    requestall = urllib2.Request(purl)
    requestall.add_header("user-agent","Mozilla/5.0")
    try:
        html_docall = urllib2.urlopen(requestall)
    except:
        return None

    htmlall=html_docall.read()
    
    soupall = BeautifulSoup(htmlall,"html.parser")
    linksall = soupall.select('form > a')

 
    for links in linksall:
        picurlall= (links.get('class'))
        if picurlall is not None:
            if 'js-keyboard-next' in picurlall:
                max_page_pos = linksall.index(links)

    max_page = int(linksall[max_page_pos-1].get_text())

    x=range(1,max_page+1)
    for i in x:
        urls.append(purl.split('-')[0]+'-'+purl.split('-')[1]+'-'+purl.split('-')[2]+'-' + str(i) + '.' + purl.split('-')[3].split('.')[-1])

    return urls
