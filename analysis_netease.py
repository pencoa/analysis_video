import urllib.request, urllib.parse, urllib.error
import re
import xml.etree.ElementTree as ET

inurl = input('please input the original url of video:\n')

m = re.search("\/([A-Z0-9]*?)\.html", inurl)
gid = m.group(1)
a = gid[-2]
b = gid[-1]

url = "http://xml.ws.126.net/video/" + a +"/" +b + "/" + "1000_" + gid + ".xml"

data = urllib.request.urlopen(url).read().decode('utf-8')
alla = ET.fromstring(data)
flv_list = alla.findall('flvUrl/flv')
flv4 = flv_list[0]
flvurl = flv4.text
print("flv_url:", flvurl)
hd_list = alla.findall('hdUrl/flv')
hd4 = hd_list[0]
hdurl = hd4.text
print("hd_url:", hdurl)