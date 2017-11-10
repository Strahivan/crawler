
from redis import Redis
from rq import Queue

redis_conn = Redis()
q = Queue(connection=redis_conn)

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
        list_of_values = []
        queued_jobs = q.job_ids
        #for job in queued_jobs:
        overall_information = redis_conn.hgetall("rq:job:6b68c737-0fdd-491f-afb8-22f976ae690d")
        descc = overall_information.get('description')
        clean_val = descc.replace("()", "")
            #val = redis_conn.get(job)
            #clean_val = rval.replace("M", "")
            #list_of_values.append(val)
            #type = redis_conn.type(key)
            #if type == KV:
            #vals = redis_conn.get(key)
            #if type == HASH:
            #vals = redis_conn.hgetall(key)
            #if type == ZSET:
            #vals = redis_conn.zrange(key, 0, -1)
        return clean_val
                #return a list of URLS

        # http://localhost:6800/schedule.json -d project=Novelship_Crawler -d spider=dynamic -d url=https://carousell.com/supremec1/
