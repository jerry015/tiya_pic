import cookielib
import urllib2
import re
from bs4 import BeautifulSoup
import ssl
import os
import time
import requests
import urls_generator
import pic_share_url_generator

def pic_down(picurls,folder_path):
    for picurl in picurls:
        request2 = urllib2.Request(picurl) 
        request2.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.170 Safari/537.36')
        request2.add_header('Accept', 'image/png,image/*;q=0.8,*/*;q=0.5')
        request2.add_header('Accept-Language', 'zh-cn,zh;q=0.8,en-us;q=0.5,en;q=0.3')
        request2.add_header('Connection', 'keep-alive')
        # request2.add_header('Host', 'img3.laibafile.cn')
        request2.add_header('Referer','http://bbs.tianya.cn/post-45-1796664-1.shtml')
        # request2.add_header('Origin', 'http://bbs.tianya.cn')

        print '=== Processing ' + str(picurls.index(picurl)+1) + '/'+ str(len(picurls)) + ' picture ==='

        try:
            picc = urllib2.urlopen(request2)
        except:
            print "Errors, skipping..."
            continue

        # folder_path = './photo/' + str(time.time()).split('.')[0] + "/"
        if os.path.exists(folder_path) == False:
            os.makedirs(folder_path)  
                
        img_name = folder_path + str(time.time()).split('.')[0] + '.' + picurl.split("/")[-1].split('.')[-1]
            
        with open(img_name, 'wb') as file:  
            file.write(picc.read())
            file.flush()
            file.close()  
            print "=== Download Finished ==="
        
        time.sleep(1) 

