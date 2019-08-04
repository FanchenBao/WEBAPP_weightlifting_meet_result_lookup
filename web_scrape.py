from typing import *
import re
import requests
from bs4 import BeautifulSoup
import json


class WebScrape:
    def __init__(self, base_url: str, start_url: str):
        self.base_url: str = base_url  # 'https://www.iwf.net'
        # two possibilities for start_url:
        # '/results/results-by-events/?event_year=' for old bw, 1998 - 2018
        # '/new_bw/results_by_events/?event_year=' for new bw, 2018 - present
        self.start_url: str = start_url

    def scrape_year(self, year: int) -> Set[str]:
        """ Scrape the web page content of each calendar year, return the urls of all the events held in that year"""
        r = requests.get(self.base_url + self.start_url + str(year))
        soup = BeautifulSoup(r.text, 'html.parser')
        # return a set of urls of events that took place in that year
        return set(a_tag['href'] for a_tag in soup.find_all(href=re.compile(r'/results/results-by-events/\?event=')))

    def scrape_event(self, event_url: str) -> str:
        """ Scrape the web page content of an event(meet), return the url of the meet result """
        r = requests.get(self.base_url + event_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return soup.iframe['src']

    def output(self, result_url: str) -> Tuple[str, List[Dict[str, str]]]:
        """  Scrape the web page content of the result, return the meet results as a list of dict, and the event id """
        m = re.search(r'event=(\d+)', result_url)
        event_id = m.group(1)  # get event_id from result_url
        r = requests.get(result_url)
        soup = BeautifulSoup(r.text, 'html.parser')
        return event_id, json.loads(soup.textarea.string)
