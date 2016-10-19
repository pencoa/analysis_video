import urllib.request, urllib.parse, urllib.error
import re
import hashlib


def get_gcid(murl):
    with urllib.request.urlopen(murl) as fhand:
        for line in fhand:
            if re.search(b'msurls', line):
                line = line.rstrip()
                line = line.split(b',')
                for item in line:
                    if re.search(b'msurls', item):
                        ids = item.split(b'/')
                        gcid = str(ids[4].upper())
                        gcid = re.sub('b|\'', '', gcid)
                        return gcid

#translate the web url into mobile url
#which consist of gcid information
inurl = 'http://vod.kankan.com/v/90/90189.shtml'
murl = re.sub('vod', 'm', inurl)

gcid = get_gcid(murl)

url1 = 'http://mp4.cl.kankan.com/getCdnresource_flv?gcid=' + gcid

response = urllib.request.urlopen(url1)
html_doc = response.read().decode("utf-8")
script_text = str(html_doc)
lines = script_text.split()

addr = lines[17]
addr = re.sub('\"', ' ', addr)
addr = addr.split()
ip = addr[1]
address = addr[3]

keys = lines[23]
key_list = re.sub('\{|\:|,|\}', ' ', keys)
keys = key_list.split()
param1 = keys[1]
param2 = keys[3]
preco = 'xl_mp43651'
key0 = preco + param1 + param2
m = hashlib.md5()
m.update(key0.encode('utf-8'))
key0 = m.hexdigest()
url = 'http://' + ip +':80/' + address + '?key=' + key0 + '&key1' + param2

print(url)