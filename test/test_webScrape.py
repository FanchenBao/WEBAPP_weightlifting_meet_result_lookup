from unittest import TestCase
from web_scrape import WebScrape


class TestWebScrape(TestCase):
    def setUp(self):
        self.ws_old = WebScrape('https://www.iwf.net', '/results/results-by-events/?event_year=')
        self.ws_new = WebScrape('https://www.iwf.net', '/new_bw/results_by_events/?event_year=')

    def test_scrape_year(self):
        self.assertEqual(self.ws_old.scrape_year(1998),
                         {
                             '/results/results-by-events/?event=158',
                             '/results/results-by-events/?event=314',
                             '/results/results-by-events/?event=96'
                         })
        self.assertEqual(self.ws_new.scrape_year(2018),
                         {
                             '/new_bw/results_by_events/?event=442',
                             '/new_bw/results_by_events/?event=444',
                             '/new_bw/results_by_events/?event=445',
                             '/new_bw/results_by_events/?event=443',
                             '/new_bw/results_by_events/?event=441'
                         })

    def test_scrape_event(self):
        old_event_urls = {
                         '/results/results-by-events/?event=158',
                         '/results/results-by-events/?event=314',
                         '/results/results-by-events/?event=96'
                        }
        old_result_urls = set()
        for event in old_event_urls:
            old_result_urls.add(self.ws_old.scrape_event(event))
        self.assertEqual(old_result_urls,
                         {
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=96',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=314',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=158'
                         })

        new_event_urls = {
                             '/new_bw/results_by_events/?event=442',
                             '/new_bw/results_by_events/?event=444',
                             '/new_bw/results_by_events/?event=445',
                             '/new_bw/results_by_events/?event=443',
                             '/new_bw/results_by_events/?event=441'
                         }
        new_result_urls = set()
        for event in new_event_urls:
            new_result_urls.add(self.ws_new.scrape_event(event))
        self.assertEqual(new_result_urls,
                          {
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=445',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=443',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=441',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=442',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=444'
                          })

    def test_output(self):
        old_result_urls = {
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=96',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=314',
                             'https://www.iwf.net/wp-content/themes/iwf/results_export.php?event=158'
                         }
        old_outputs = set()
        for result in old_result_urls:
            all_athletes = self.ws_old.output(result)
            old_outputs.add(all_athletes[0]['name'])
        self.assertEqual(old_outputs, {'LI Yunli', 'LUO Xiaoqin', 'LI Xuezhao'})

        new_result_urls = {
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=445',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=443',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=441',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=442',
                            'https://www.iwf.net/wp-content/themes/iwf/results_export_newbw.php?event=444'
                          }
        new_outputs = set()
        for result in new_result_urls:
            all_athletes = self.ws_new.output(result)
            new_outputs.add(all_athletes[0]['name'])
        self.assertEqual(new_outputs,
                         {'ZHANG Rong', 'BERRIO ZULUAGA Manuela Andrea',
                          'SUKCHAROEN Thunya', 'RANDAFIARISON Rosina',
                          'BERRIO ZULUAGA Manuela Andrea'})
