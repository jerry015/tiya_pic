import cookielib
import urllib2
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
import requests

def pic_urls_gen(web_url):
    pic_urls = []

    request = urllib2.Request(web_url)
    request.add_header("user-agent","Mozilla/5.0")
    try:
        html_doc = urllib2.urlopen(request)
    except:
        return None

    html=html_doc.read()

    soup = BeautifulSoup(html,"html.parser")
    links = soup.find_all('img')

    for link in links:
        picurl= (link.get('original'))
        # print picurl
        if ((picurl is not None) and (('jpg' in picurl) or ('JPG' in picurl))):
                picurl = picurl.split('jpg')[0] + 'jpg'
                pic_urls.append(picurl)

    return pic_urls

