# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from zads_spider.items import ZadsSpiderItem
import re
class ZadsSpider(scrapy.Spider):
    name = "zads"
    allowed_domains = ["zreading.cn"]
    start_urls = (
        'http://www.zreading.cn/',
    )

    def parse(self, response):
        if response.url.endswith('html'):
            item = self.parsePaperContent(response)

        else:
            #从列表中获取所有文章链接
            sel = Selector(response)
            links = sel.xpath('//*[id("content")]/article/header/h2/a/@href').extract()
            for link in links:
                print link
                yield Request(link, callback=self.parse)

            #获取下一页
            next_pages = sel.xpath('//*[id("content")]/div/a[@class="next"]/@href').extract()
            if len(next_pages) !=0:
                yield Request(next_pages[0],callback=self.parse)

        yield item

    def parsePaperContent(self,response):
        print u'正在爬取内容页...'
        page_id = response.url.split('/')[-1].split('.')[0]
        r  =re.match(r'\d+',response.url.split('/')[-1])
        page_id = r.group()
        zding = ZadsSpiderItem('')
        sel = Selector(response)

        #获取标题
        title = sel.xpath("//div[@id='content']/article/header/h2/text()").extract()[0]
        s_title = title.encode("utf-8")
        zding['title'] = s_title.lstrip().rstrip()

        #获取发布时间
        pub_date = sel.xpath('//*[@id="'+page_id+'"]/div[2]/span[1]/text()').extract()[0]
        s_pub_date = pub_date.encode("utf-8")
        zding['pub_date'] = s_pub_date.lstrip().rstrip()

        #获取作者
        author = sel.xpath('//*[@id="'+page_id+'"]/div[2]/span[2]/a/text()').extract()[0]
        s_author = author.encode("utf8")
        zding['author'] = s_author.lstrip().rstrip()


        #add tags including type and paper tags

        tags = sel.xpath('//*[@id="'+page_id+'"]/div[2]/a/text()').extract()
        tags = [s.encode('utf8') for s in tags]
        zding['types'] = tags[0]
        zding['tags'] = "+".join(tags[1:])

        #add view count
        views = sel.xpath('//*[@id="'+page_id+'"]/div[2]/span[3]/text()').extract()[0]
        r = re.search(r'\d+',views)
        view_count = int(r.group())
        zding['view_count'] = view_count
        #add content
        content = sel.xpath('//*[@id="'+page_id+'"]/div[3]/p/text()').extract()
        zding['content'] = "\n".join(content)

        #return the item
        return zding


