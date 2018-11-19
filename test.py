import urls_generator
import pic_share_url_generator
import pic_downloader
import time

import sys


purl= sys.argv[1]

urls = urls_generator.urls_gen(purl)

# print purl.split('/')[0] + '//' + purl.split('/')[2] + '/'
# print urls

picurls=pic_share_url_generator.pic_urls_gen(urls[2])
print picurls
# pic_downloader.pic_down(picurls)

