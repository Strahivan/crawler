import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from Novelship_Crawler.items import NovelshipCrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector
from scrapy_splash import SplashRequest

class sellerSpider(CrawlSpider):
    name = 'seller'
    allowed_domains = ['carousell.com']
    start_urls = ['https://carousell.com/khvnmrkt/', 'https://carousell.com/allen895/']

    rules = (Rule (LinkExtractor(allow=(''),
    restrict_xpaths=('//*[@id="productCardThumbnail"]'))
    ,callback="parse_items", follow=True),)


    #The next To-Do is to click on the "next-page" button and crawl
    # xPath for next-page button:
    #/html/body/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/div[3]/ul/li[2]/a

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
            return items

"""
This method here is needed for a scrapy_splash connection to re-render the .js
relevant content because scrapy is not rendering .js content at all

- But for carousell.com, that .js-rendering is not needed
"""
#    def start_requests(self):
#        for url in self.start_urls:
#            yield SplashRequest(url, self.parse_items, args={'wait': 0.5})
