# -*- coding: utf-8 -*-
import scrapy
from hwsina.items import HwsinaItem
try:
    from urllib import urlencode
except ImportError:
    from urllib.parse import urlencode

class Hwsina(scrapy.Spider):
    name='hwsina'
    comp="特金会"
    def start_requests(self):
        pages = []
        comp = self.comp.encode('gbk')
        d = {'q':comp}
        pname = urlencode(d)
        for i in range(1,10):
            allowed_domains = ["http://search.sina.com.cn/"]
            start_urls = "http://search.sina.com.cn/?%s&c=news&&num=20&col=1_7&page=%s" %(pname, i)
            url = "http://search.sina.com.cn/?%s&c=news&&num=20&col=1_7&page=%s" %(pname, i)
            #start_urls = "http://search.sina.com.cn/?q=%CC%D8%BD%F0%BB%E1&range=all&c=news&sort=time"
            page = scrapy.Request(start_urls, dont_filter = True)
            pages.append(page)
            return pages
    def parse(self, response):
        item = HwsinaItem()
        items = []
        divs = response.xpath('//*[@id="result"]/div/div')
        if not divs:
            self.log("Not found --%s"%response.url)
        for div in divs:
            item['title'] = div.xpath('h2/a/text()').extract()[0]
            item['source'],item['date'],item['time'] = div.xpath('h2/span/text()').extract()[0].split()
            item['url'] = div.xpath('h2/a/@href').extract()[0]
            item['abstract'] = div.xpath('p/text()').extract()[0]
            items.append(Request(url = item['url'], meta = {'item':item}, callback = self.detail, dont_filter = True))
            #return items
            print('URL is: {}'.format(url))
            print('TITLE is: {}'.format(title))
            print('SOURCE is: {}'.format(source))
            print('ABSTRACT is: {}'.format(abstract))

    def paras(self, response):
        div = div.xpath('//*[@id="artibody"]/p')
        if not div:
                self.log("Not found %s"%response.url)
        item = response.meta['item']
        print(response.url)
        content = ""
        for x in response.xpath('//*[@id="artibody"]/p'):
            content+=x.xpath('text()').extract()[0]
        item['content'] = content
        return item
    if __name__ == "__main__":
        compRawStr = '百度'
    # Dealing with character encoding
        comp = compRawStr.encode('gbk')
        d = {'q': comp}
        pname = urlencode(d)
    # Scraping and printing the first two pages
        for page in range(3)[1:]:
            newsData = parse()
        for ky in newsData:
            print('\001'.join([ky] + newsData[ky])) # "\001" as separator
