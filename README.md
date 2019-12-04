[![Python 3.7](https://img.shields.io/badge/python-3.7-blue.svg)](https://www.python.org/downloads/release/python-370/) [![Flask v1.1.1](https://img.shields.io/badge/flask-v1.1.1-blue)](http://flask.palletsprojects.com/en/1.1.x/)

# Weightlifting Meet Result Lookup

## Introduction
This is a simple web app to query all weightlifting meet results available on [IWF Official Website](https://www.iwf.net) from 1998 to August, 2019. Data were scraped from IWF's website and stored on heroku's postgresql database. To try out the web app, click here: [https://weightlifting-result-stage.herokuapp.com/](https://weightlifting-result-stage.herokuapp.com/).

The motivation behind this project is that the process of searching for weightlifting meet results directly from IWF official website involves more mouse clicks than I would like. I prefer a single portal that allows users to use whatever query combination they like, e.g. a certain gender of a certain country, a certain weight class in a certain meet, specific athlete at certain meet, etc. [Weightlifting Meet Result Lookup](https://weightlifting-result-stage.herokuapp.com/) provides such portal with easy-to-navigate user interface.

## Webapp Snapshot
![webapp snapshot]()

## Issues And ToDo
* Since the heroku database already contains more rows than `hobby-dev` tier allows (10,000 rows limit), no more insert action can be executed until number of rows drop below the free-tier limit or the database is upgraded. Currently, I have no plan of paying for a bigger database. That's why the web app only supports results up till August, 2019.
* IWF's official website is not the only source for meet results. [IWRP](http://iwrp.net/events) is also a great source, providing non-IWF sanctioned meet results and even data from as early as 1928. Incorporating IWRP's data will definitely be very helpful.
