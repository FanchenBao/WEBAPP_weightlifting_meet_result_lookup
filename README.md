[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Flask v1.1.1](https://img.shields.io/badge/flask-v1.1.1-blue)](http://flask.palletsprojects.com/en/1.1.x/)

# Weightlifting Meet Result Lookup

## Introduction
This is a simple web app to query all weightlifting meet results available on [IWF Official Website](https://www.iwf.net) from 1998 to August, 2019. Data were scraped from IWF's website and stored on heroku's postgresql database. To try out the web app, click here: [https://weightlifting-result-stage.herokuapp.com/](https://weightlifting-result-stage.herokuapp.com/).

The motivation behind this project is that the process of searching for weightlifting meet results directly from IWF official website involves more mouse clicks than I would like. I prefer a single portal that allows users to use whatever query combination they like, e.g. a certain gender of a certain country, a certain weight class in a certain meet, specific athlete at certain meet, etc. [Weightlifting Meet Result Lookup](https://weightlifting-result-stage.herokuapp.com/) provides such portal with easy-to-navigate user interface.

## Webapp Snapshot
![webapp snapshot]()

## Q & A
### Why data extend only to August, 2019?
Because I have exceeded the row limit (10,000) of heroku's `hobby-dev` tier for postgresql database. Unless I upgrade or ingeniously improve database structure, I am stuck with August, 2019. In fact, currently the database already contained about 20k rows. Heroku is kind enough to allow me to keep all the rows already migrated there, but no more insertion is allowed.

### What about weightlifting results before 1998 or non-IWF sanctioned meets?
For old or non-IWF sanctioned meet results, the best aggregated source is [IWRP](http://iwrp.net/events). We can also crawl websites of all major continental/national weightlifting federations to get non-IWF sanctioned meets. This is certainly doable, but contingent on resolving the database issue first.

### Why is there `stage` in the web app URL?
Because the current web app version is still considered as staging, not production yet. Considering my schedule and focus, this web app will stay as "stage" for a long time.