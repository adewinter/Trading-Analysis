import json
import os

__author__ = 'adewinter'

import requests
from pyquery import PyQuery as pq
from raw_data import *


class FinScraper:
    base_url = 'http://feeds2.mcgbfa.com/psgonline/financials.asp?ticker='
    default_ticker = 'KIO'
    backup_folder = os.path.join(os.path.abspath(__file__),'..','fin_data')
    def __init__(self, symbol):
        """
        Initiate a Finance page scraper.
        symbol is the stock symbol used to search for the page, e.g. 'KIO' or 'HLM'
        """
        if not symbol:
            self.symbol = self.default_ticker
        else:
            self.symbol = symbol
        self.raw_text = ''
        self.json = {}
        self.parsed_xml = ''

    def _get_page_url(self):
        return '%s%s' % (self.base_url, self.symbol)

    def get_fin_text(self):
        """
        Downloads the financial data: making it available to the object and saving a backup to disk
        """
        #test if we already have a cached copy
        path = os.path.join(self.backup_folder,'%s_financial_data.html' % self.symbol)
        self.raw_text = ''
        try:
            f = file(path,'r')

            for line in f:
                self.raw_text += line
            f.close()
        except IOError as e:
            print 'No cached copy file found.'
            
        if not self.raw_text:
            print 'No cached copy of %s found. Pulling from online data...' % self.symbol
            r = requests.get(self._get_page_url())
            self.raw_text = r.text
        else:
            print 'cached copy of %s found, using that instead!' % self.symbol
        # Save the raw text

        print 'Saving backup copy of fin data to: %s' % path
        f = file(path,'w')
        f.write(self.raw_text)
        f.close()
#        self.raw_text = KIO_STRING
        return self.raw_text

    def set_ticker(self, symbol):
        self.__init__(symbol)

    def table_to_json(self):
        self.rows = {}
        def parse_row(i,row):
            parse_row.name = ''
            parse_row.values = []
            def parse_col(i,col):
                if i == 0:
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
            self.json.update(row_dict)

        self.parsed_xml = pq(self.raw_text)
        self.parsed_xml.find('tr').each(parse_row)
        body_len = self.parsed_xml.find('html>body>form>a:eq(1)').find('table:eq(0)').children().length
        if not body_len:
            self.has_data = False
        else:
            self.has_data = True
        
        print 'Done parsing!'
        

                          

    def parse(self):
        self.get_fin_text()
        self.table_to_json()
        return self




def print_dict(d):
    for k in d.keys():
        print '%s: %s' % (k, d[k])

#
#f = FinScraper('KIO')
#KIO_json = f.parse().json




#http://feeds2.mcgbfa.com/psgonline/financials.asp?ticker=KIO