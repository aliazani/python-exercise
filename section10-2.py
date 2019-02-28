import re
import urllib.request


class Browser:
    instances = {}
    count = 0

    def __init__(self, url):
        self.url = url
        if not Browser.check_available(url):
            raise Exception
        self.instances.update({url: self})
        # self.count += 1
        self.__class__.count += 1
        self._text = ''

    @property
    def links(self):
        pat = r'href=[\'"]?(https?[^\'" >]+)'
        links = re.findall(pat, self.text)
        browsers = []
        for i in links:
            try:
                browsers.append(Browser(i))
            except:
                pass
        return browsers

    @classmethod
    def get_unread(cls):

        out = []
        for v in cls.instances.values():
            if v._text == '':
                out.append(v)
        return out

    @property
    def text(self):
        if self._text == '':
            req = urllib.request.urlopen(self.url)
            text = req.read()
            text = str(text)
            self._text = text
        return self._text

    @classmethod
    def check_available(cls, address):
        res = cls.instances.get(address, None)
        if res is None:
            return True
        else:
            return False


Browser.count
urls = ['https://www.google.com',
        'http://wttr.in/tehran', ]
for u in urls:
    try:
        b1 = Browser(u)
        # print(b1.text)
        print(b1.links)
        # for i in range(100):
        #     print(b1.text)
    except Exception:
        print(f"you've defined url = {u} before")

unread = Browser.get_unread()
print(unread)
