import urllib.request
import urllib.parse
import re
import sys

url_dict = {
    'page1': {'name':'普通落地页', 'url':'url_1', 'keyword':'立即体验', 'data': {}},
    'page2': {'name':'带mcode落地页', 'url':'url_2', 'keyword':'免押体验', 'data':{}},
    'page3': {'name':'登录页面', 'url':'url_3', 'keyword':'立即开启', 'data': {}},
    'page4': {'name':'帮助中心', 'url':'url_4', 'keyword':'GoogleAnalyticsObject', 'data': {}},
    'page5': {'name':'登录接口', 'url':'url_5', 'keyword':'10004', 'data':{'Phone':'33333', 'SmsCode':'180501'}},
}

class url_check(object):
    def __init__(self, url, keyword, data):
        self.url = url
        self.keyword = keyword
        self.data = data
    
    def get_url_content(self):
        try:
            if len(self.data) == 0:
                req = urllib.request.urlopen(self.url)
            else:
                self.data = urllib.parse.urlencode(self.data).encode('utf8')
                req = urllib.request.urlopen(self.url, self.data)
        except urllib.error.HTTPError as e:
            #print('urllib.error.HTTPError error')
            print(1)
        else:
            values = req.read().decode('utf8')
            return values

    def find_keyword(self, values):
        if re.search(self.keyword, values):
            print('0')
        else:
            print('1')
        #print(values)

if __name__ == '__main__':
    URL = url_check(url_dict[sys.argv[1]]['url'], url_dict[sys.argv[1]]['keyword'], url_dict[sys.argv[1]]['data'])
    values = URL.get_url_content()
    URL.find_keyword(values)
