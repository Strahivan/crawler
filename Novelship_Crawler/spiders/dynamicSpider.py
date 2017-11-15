# -*- coding: utf-8 -*-
#
# Autor: Strahinja Ivanovic
#
# A scrapy-crawl component which is used for scraping a
# sellers-page on carousell. Contains an integrated (data)-pipeline
# to a local mongodb where the fetched items are stored

import scrapy
from scrapy.http import Request
from scrapy.selector import HtmlXPathSelector
from scrapy.linkextractors import LinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from Novelship_Crawler.items import NovelshipCrawlerItem

# It's important to inherit from CrawlSpider and not from BaseSpider
# With a BaseSpider you're not able to access the rule-object
class dynamicSpider(CrawlSpider):

    name = 'dynamic'
    allowed_domains = ['carousell.com']
    start_urls = ['https://carousell.com/littletwinstars82/']

"""
restrict_xpaths = Defines the entry point for the LinkExtractor.
The LinkExtractor is extracting the links from the given xPath and returns them
as a list. Afterwards the method which is specified in 'callback' is getting
executed on each link.
"""
    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="productCardThumbnail"]'))
    ,callback="parse_items", follow=True),)

    # scrapes a single product
    def parse_items(self, response):
        hxs = HtmlXPathSelector(response)
        items = []
        desc = hxs.select("//html/body/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/section/div/div/div[1]/article")

        for desc in desc:
            item = NovelshipCrawlerItem()
            item ["title"] = desc.select("h1/text()").extract()
            item ["price"] = desc.select("div/div[2]/span/text()").extract()
            item ["customer_id"] = desc.select("div/div[1]/a/text()").extract()
            item ["location"] = desc.select("div/div[3]/span/text()").extract()
            items.append(item)

            yield item
            #return items


"""
This method here is needed for parameterized scrapyd calls. It assigns a given
url-parameter (last -d from the shell-call) and adjusts the start_urls

Example: curl http://localhost:6800/schedule.json -d project=Novelship_Crawler
-d spider=dynamic -d url=https://carousell.com/supremec1/

"""
    #def __init__(self, *args, **kwargs):
    #    super(dynamicSpider, self).__init__(*args, **kwargs)
    #    self.start_urls.append(kwargs.get('url'))

"""
This method here is needed for a scrapy_splash connection to re-render the .js
relevant content because scrapy is not rendering .js content at all

- But for carousell.com, that .js-rendering is not needed
"""
#    def start_requests(self):
#        for url in self.start_urls:
#            yield SplashRequest(url, self.parse_items, args={'wait': 0.5})
