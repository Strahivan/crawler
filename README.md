# Novelship-Crawler

### Deployment

Two branches:

- `Master`: Branch for Heroku deployment
- `Local`: Branch for Local deployment

To switch between different deployment targets (Heroku or local installation)
the following lines of code need to be adjusted:

##### scrapy.cfg [12-16]

```python
[deploy]
url = https://novelship-crawler.herokuapp.com/
project = novelship-crawler
username = Cabron
password = call_me_patron!
```

##### main.py [57]

```python
r = requests.post("https://novelship-crawler.herokuapp.com/schedule.json", data=payload)
```

##### settings.py [21-22]

```python
MONGO_URI = 'mongodb://localhost:27017'
MONGO_DATABASE = 'novelship-sandbox'
```


### Installation

- Initialize virtualenv
- Install requirements.txt
- Start Redis
- Start scrapyd (crawler has to be deployed)
- Start Mongodb
- Start Flask (flask run)

### Other insights

- Flask needs gunicorn as wrapper to run on Heroku
- Untested: Don't know whether crawler writes in mongodb if you schedule a dynamic-spider crawl from scrapyd.
- CrawlerRunner and CrawlerProcess cause ‘reactor not restarting’-bug:  This is a serious bug because the ReactorNotRestartable-Exception is raised by Twister, which is heavily used by Scrapy. Means in our context: Every time you schedule a crawlerProcess, the reactor.stop() method will be called after crawling. There's a conflict for flask and scrapy both using twister.
- URL for scheduling a crawl via scrapyd: http://localhost:6800/schedule.json -d project=Novelship_Crawler -d spider=dynamic -d url= https://carousell.com/supremec1/
