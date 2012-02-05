import json

__author__ = 'adewinter'

import requests
from pyquery import PyQuery as pq
from raw_data import *


class finScraper:
    base_url = 'http://feeds2.mcgbfa.com/psgonline/financials.asp?ticker='

    def __init__(self, symbol):
        """
        Initiate a Finance page scraper.
        symbol is the stock symbol used to search for the page, e.g. 'KIO' or 'HLM'
        """
        self.symbol = symbol
        self.raw_text = ''
        self.json = {}
        self.parsed_xml = ''

    def _get_page_url(self):
        return '%s%s' % (self.base_url, self.symbol)

    def get_fin_text(self):
#        r = requests.get(self._get_page_url())
#        self.raw_text = r.text
        self.raw_text = KIO_STRING
        return self.raw_text

    def set_ticker(self, symbol):
        self.__init__(symbol)

    def table_to_json(self):
        self.rows = {}
        def parse_row(i,row):
            parse_row.name = ''
            parse_row.values = []
            def parse_col(i,col):
                if i==0:
                    if not pq(col).text():
                        parse_row.name = ''
                        return
                    parse_row.name = pq(col).text()
                else:
                    if not parse_row.name:
                        return
                    parse_row.values.append(pq(col).text().strip().replace(',',''))


            r = pq(row)
            r.children('td').each(parse_col)
            row_dict = {parse_row.name: parse_row.values}
            self.json.update(row_dict);

        self.parsed_xml = pq(f.raw_text)
        self.parsed_xml.find('tr').each(parse_row)

        print 'Done parsing!'
        print 'Dict: %s' % print_dict(self.json)
        

                          

    def parse(self):
        self.get_fin_text()
        self.table_to_json()
        return self




def print_dict(d):
    for k in d.keys():
        print '%s: %s' % (k, d[k])


f = finScraper('KIO')
KIO_json = f.parse().json




#http://feeds2.mcgbfa.com/psgonline/financials.asp?ticker=KIO