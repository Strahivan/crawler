# -*- coding: utf-8 -*-
#
# Autor: Strahinja Ivanovic
#
# Obsolete scrapy-crawl component

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Novelship_Crawler.items import NovelshipCrawlerItem

class productSpider(BaseSpider):
    name = "product"
    allowed_domains = ["carousell.org"]
    start_urls = ["https://carousell.com/p/supreme-balck-bogo-hoody-131465119/?ref=profile&ref_referrer=%2Fallen895%2F&ref_sId=4093106"]

    def parse(self, response):
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
            return items
