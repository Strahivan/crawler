from flask import Flask
import scrapy
from spiders.dynamicSpider import dynamicSpider
from scrapy.crawler import CrawlerProcess, CrawlerRunner

from twisted.internet import reactor
import os
from subprocess import call

app = Flask(__name__)
spi = dynamicSpider()
process = CrawlerProcess()

if __name__ == 'Novelship_Crawler.main':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/crawl/<string:domain>/<string:account_id>')
def crawlSeller(domain, account_id):
    crawlURL = 'https://'+domain+ '.com/'+account_id
    process.crawl(spi, start_urls=['https://'+domain+ '.com/'+account_id])
    process.start()

    #To-Do send .json response

    #runner = CrawlerRunner()
    #runner.crawl(spi, start_urls=['https://'+domain+ '.com/'+account_id])
    #d = runner.join()
    #d.addBoth(lambda _: reactor.stop())

    #spi.start_urls=str(crawlURL)
    #os.system("scrapy crawl dynamic")
    #os.system("scrapy crawl dy -a start_requests="+str(crawlURL))

    #baue crawlURL zusammen
    #https://carousell.com/allen895/
    #spi.start_req(domain,account_id)
    return 'crawled:'+crawlURL


#spider.start_urls = ['http://google.com']


#scrapy crawl dmoz -a start_requests="this"

#call(["ls", "-l"])

#subprocess.call(crop, shell=True)

#os.system('your_command')
