from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from Novelship_Crawler.items import NovelshipCrawlerItem

class MySpider(BaseSpider):
    name = "carousell"
    allowed_domains = ["carousell.org"]
    # start_urls = ["https://carousell.com/allen895/"]
    start_urls = ["https://carousell.com/p/supreme-balck-bogo-hoody-131465119/?ref=profile&ref_referrer=%2Fallen895%2F&ref_sId=4093106"]

    # hier dann auch nochmal Gedanken machen bzgl. der Unterteilung der Methoden was am Meisten Sinn macht

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
            # price = desc.select("a/@href").extract()


#Scrapy crawl carousell

# XPath expressions for the single items:
# Title = /html/body/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/section/div/div/div[1]/article/h1
# Preis = /html/body/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/section/div/div/div[1]/article/div/div[2]/span
# Seller = /html/body/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/section/div/div/div[1]/article/div/div[1]/a
# Location = /html/body/div[2]/div/div[1]/div[2]/div/div[3]/div[2]/section/div/div/div[1]/article/div/div[3]/span


# description = /html/body/div[2]/div/div[1]/div[2]/div/div[4]/div[1]/div/div/div/div/div[1]/div/p
