from unittest import TestCase
from web_scrape import WebScrape


class TestWebScrape(TestCase):
    def setUp(self):
        self.ws = WebScrape('https://www.iwf.net', '/results/results-by-events/?event_year=')

    def test_scrape_year(self):
        self.assertEqual(self.ws.scrape_year(1998),
                         {
                             '/results/results-by-events/?event=158',
                             '/results/results-by-events/?event=314',
                             '/results/results-by-events/?event=96'
                         })

    def test_scrape_event(self):
        event_urls = {
                         '/results/results-by-events/?event=158',
                         '/results/results-by-events/?event=314',
                         '/results/results-by-events/?event=96'
                        }
        result_urls = set()
        for event in event_urls:
            result_urls.add(self.ws.scrape_event(event))
        self.assertEqual(result_urls,
                         {
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=96',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=314',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=158'
                         })

    def test_output(self):
        result_urls = {
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=96',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=314',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=158'
                         }
        outputs = set()
        for result in result_urls:
            event_id, all_athletes = self.ws.output(result)
            outputs.add((event_id, all_athletes[0]['name']))
        self.assertEqual(outputs,
                         {
                             ('96', 'LI Yunli'),
                             ('158', 'LUO Xiaoqin'),
                             ('314', 'LI Xuezhao')
                         })
