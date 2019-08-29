#有道翻译爬虫
import urllib.request
import urllib.parse
import json

content = input("请输入需要翻译的内容")
url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=http://www.youdao.com/"
data = {}
data['type'] = 'AUTO'
data['i'] = content
data['doctype'] = 'json'
data['xmlVersion'] = '1.6'
data['keyfrom'] = 'fanyi.web'
data['ue'] = 'UTF-8'
data['typoResult'] = 'true'
data = urllib.parse.urlencode(data).encode('utf-8')

#修改User-Agent
#method 1
head = {}
head['Referer'] = 'http://fanyi.youdao.com'
head['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36X-Requested-With:XMLHttpRequest'
req = urllib.request.Request(url, data, head)

#method 2
'''req = urllib.request.Request(url, data)
req.add_header('Referer', 'http://fanyi.youdao.com')
req.add_header('User-Agent', 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36X-Requested-With:XMLHttpRequest')
'''
resonse = urllib.request.urlopen(req)
html = resonse.read().decode('utf-8')
target = json.loads(html)
print("翻译结果: %s" % (target['translateResult'][0][0]['tgt']))