# -*- coding: utf-8 -*-
#
# Autor: Strahinja Ivanovic
#
# Generic redis-queue handler which is called by the flask-app component.
# Contains read and write methods for the redis-job queue. We use redis-jobs
# just to store urls which have to be crawled by scrapy.

import os
import urlparse
from rq import Queue
from redis import Redis

# Get environment variable for Redis (REDISTOGO_URL)
redis_url = os.getenv('REDISTOGO_URL')
urlparse.uses_netloc.append('redis')
url = urlparse.urlparse(redis_url)

# Connect to Redis
conn = Redis(host=url.hostname, port=url.port, db=0, password=url.password)
q = Queue(connection=conn)

class redishandler():

    # Schedules a new job with input_HTML = URL (from the HTML-Input field)
    def schedule(self, input_HTML):
        q.enqueue(input_HTML)
        queued_jobs = q.jobs
        return queued_jobs

    # Get a list of existing jobs in redis-queue
    def getjobs(self):
        queued_jobs = q.jobs
        return queued_jobs

    # Executes all jobs from the redis-queue
    def execute_jobs(self):
        list_of_clean_values = []
        queued_jobs = q.job_ids

        for job in queued_jobs:
            # preparing incoming queue key for redis-<key><value> mapping
            var = job.encode("utf-8")
            var2 = var.replace("[", "")
            var3 = var2.replace("]", "")
            generic_beginning = "rq:job:" + var3

            # get redis value for key
            overall_information = conn.hgetall(generic_beginning)
            descc = overall_information.get('description')
            #prepare value / the url for crawling and return it as a list
            clean_val = descc.replace("()", "")
            list_of_clean_values.append(clean_val)
        return list_of_clean_values
