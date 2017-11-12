
from redis import Redis
from rq import Queue

redis_url = os.getenv('REDISTOGO_URL', 'redis://localhost:6379')
redis = redis.from_url(redis_url)

#redis_conn = Redis()
q = Queue(connection=redis)

class redishandler():

    def schedule(self, input_HTML):
        q.enqueue(input_HTML)
        #queued_job_ids = q.job_ids
        queued_jobs = q.jobs
        #print(q.job_ids)
        return queued_jobs

    def getjobs(self):
        queued_jobs = q.jobs
        #print(q.job_ids)
        return queued_jobs

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
            overall_information = redis_conn.hgetall(generic_beginning)
            descc = overall_information.get('description')
            #prepare value / the url for crawling and return it as a list
            clean_val = descc.replace("()", "")
            list_of_clean_values.append(clean_val)
        return list_of_clean_values #list_of_clean_values



        # http://localhost:6800/schedule.json -d project=Novelship_Crawler -d spider=dynamic -d url=https://carousell.com/supremec1/
