# -*- coding: utf-8 -*-
#
# Autor: Strahinja Ivanovic
#
# Controller-component for scheduling crawl-jobs via flask.
# Interacts between the User-Interface, Redis and scrapyd-server.
# Scrapy crawler are just scheduled via scrapyd.


import os
import json
import scrapy
import requests
from rq import Queue
from rq.job import Job
from server.worker import conn
from server.redishandler import redishandler
from scrapy.crawler import CrawlerProcess, CrawlerRunner
from flask import Flask, make_response,render_template, request, jsonify

# Initialize flask application and redishandler
app = Flask(__name__)
app.config.from_pyfile('config.cfg')
rdhandler = redishandler()

# Main (landing) page
@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.mimetype = 'text/html'
    return resp

# After clicking on 'submit-button' below carousell-crawl input-field
@app.route('/', methods=['POST'])
def schedule_redis():
    text = request.form['Carousell-link-to-redis']
    # add job (or rather url) to redis-queue
    all_jobs=rdhandler.schedule(text)
    app.logger.info('%s added to queue', all_jobs)
    resp = make_response(render_template('index.html'))
    return resp

# Render html with all existing jobs at redis-queue
@app.route('/show')
def show_jobs():
    list_of_jobs = rdhandler.getjobs()
    return render_template('show.html', list_of_jobs=list_of_jobs)

# Execute all redis-jobs
@app.route('/run')
def run_job():
    url_LIST = rdhandler.execute_jobs()
    app.logger.info('here is what happend: %s' , url_LIST)
    # Send a request to scrapyd for each job (url)
    for ur in url_LIST:
        payload = {'project': 'Novelship_Crawler', 'spider': 'dynamic' , 'url': ur }
        r = requests.post("https://novelship-crawler.herokuapp.com/schedule.json", data=payload)
    return r.text
