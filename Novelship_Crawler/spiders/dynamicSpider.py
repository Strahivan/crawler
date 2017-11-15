import scrapy
from scrapy.http import Request
from scrapy.contrib.spiders import CrawlSpider, Rule
from Novelship_Crawler.items import NovelshipCrawlerItem
from scrapy.linkextractors import LinkExtractor
from scrapy.selector import HtmlXPathSelector

class dynamicSpider(CrawlSpider):
    name = 'dynamic'
    allowed_domains = ['carousell.com']
    start_urls = ['https://carousell.com/allen895/']#, 'https://carousell.com/allen895/']

    # dynamic assignment of the scrapyd-url parameter
    #def __init__(self, *args, **kwargs):
    #    super(dynamicSpider, self).__init__(*args, **kwargs)
    #    self.start_urls.append(kwargs.get('url'))

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
            yield item
            #yield scrapy.Request(self.main_url, callback=self.parse_items)

            #return items


#def start_req(self, domain, account_id):
#    yield Request(crawlURL, self.parse_items)
