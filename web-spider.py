import time
import urls_generator
import pic_share_url_generator
import pic_downloader
import sys

purl = sys.argv[1]
urls = urls_generator.urls_gen(purl)
folder_path = './photo/' + str(time.time()).split('.')[0] + "/"
if urls is not None:
    for url in urls:
        print "=== Processing "+ str(urls.index(url)+1) + "/" + str(len(urls)) + " url ==="
        picurls = pic_share_url_generator.pic_urls_gen(url)
        if picurls is not None:
            pic_downloader.pic_down(picurls,folder_path)
            time.sleep(5)
