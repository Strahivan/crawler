from flask import Flask, make_response,render_template, request, jsonify
import scrapy
#from crawler.Novelship_Crawler.spiders.dynamicSpider import dynamicSpider
from scrapy.crawler import CrawlerProcess, CrawlerRunner

import os
import json
from redishandler import redishandler
from rq import Queue
from rq.job import Job
from worker import conn

app = Flask(__name__)
app.config.from_pyfile('config.cfg')
rdhandler = redishandler()

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.mimetype = 'text/html'
    return resp

@app.route('/', methods=['POST'])
def schedule_redis():
    text = request.form['Carousell-link-to-redis']
    all_jobs=rdhandler.schedule(text)
    app.logger.info('%s added to queue', all_jobs)
    resp = make_response(render_template('index.html'))
    return resp

@app.route('/show')
def show_jobs():
    list_of_jobs = rdhandler.getjobs()
    return render_template('show.html', list_of_jobs=list_of_jobs)





#spi = dynamicSpider()
#process = CrawlerProcess()
# Needs to be modified for Heroku
#if __name__ == 'Novelship_Crawler.main':
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)


#@app.route('/crawl/<string:domain>/<string:account_id>')
#def crawlSeller(domain, account_id):
#    crawlURL = 'https://'+domain+ '.com/'+account_id
#    process.crawl(spi, start_urls=['https://'+domain+ '.com/'+account_id])
#    process.start()

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
#    return 'crawled:'+crawlURL
