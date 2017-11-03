
from redis import Redis
from rq import Queue

redis_conn = Redis()
q = Queue(connection=redis_conn)

class redishandler():

    def schedule(self,input_HTML):
        q.enqueue(input_HTML)
        #queued_job_ids = q.job_ids
        queued_jobs = q.jobs
        #print(q.job_ids)
        return queued_jobs

    def getjobs(self):
        queued_jobs = q.jobs
        #print(q.job_ids)
        return queued_jobs
