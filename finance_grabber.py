import json
import os
from os.path import split as ssplit
import requests
from pyquery import PyQuery as pq
from raw_data import *


class FinScraper:
    base_url = 'http://feeds2.mcgbfa.com/psgonline/financials.asp?ticker='
    market_url = "http://www.fin24.com/ChartData.ashx?&ticker=%s&interval=Year&period=5"
    default_ticker = 'KIO'
    here_folder = ssplit(os.path.abspath(__file__))[0]
    backup_folder = os.path.join(here_folder,'fin_data')
    backup_market_folder = os.path.join(here_folder,'market_data')

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
        self.raw_market_text = ''
        self.json = {}
        self.market_json = ''
        self.parsed_xml = ''

    def _get_page_url(self):
        return '%s%s' % (self.base_url, self.symbol)

    def _get_market_data_url(self):
        return self.market_url % self.symbol

    def get_fin_text(self):
        """
        Downloads the financial data: making it available to the object and saving a backup to disk
        """
        #test if we already have a cached copy
        path = os.path.join(self.backup_folder,'%s_financial_data.html' % self.symbol)
        market_path = os.path.join(self.backup_market_folder, '%s_market_data.html' % self.symbol)
        self.raw_text = ''
        self.raw_market_text = ''
        try:
            mf = file(market_path, 'r')
            for line in mf:
                self.raw_market_text += line
            mf.close()
        except IOError as e:
            print 'No cached copy of market data found. %s' % self.symbol

        try:
            f = file(path,'r')
            for line in f:
                self.raw_text += line
            f.close()
        except IOError as e:
            print 'No cached copy of financial data found. %s' % self.symbol
            
        if not self.raw_text:
            print 'No cached copy of %s found (Financial Data). Pulling from online data...' % self.symbol
            r = requests.get(self._get_page_url())
            self.raw_text = r.text
        else:
            print 'cached copy of %s found (Financial Data), using that instead!' % self.symbol
        # Save the raw text

        if not self.raw_market_text:
            print 'No cached copy of %s found (Market Data). Pulling from online data...' % self.symbol
            mr = requests.get(self._get_market_data_url())
            self.raw_market_text = mr.text
        else:
            print 'cached copy of %s found, using that instead!' % self.symbol
        # Save the raw text


        print 'Saving backup copy of Financial data for %s to: %s' % (self.symbol, path)
        f = file(path,'w')
        f.write(self.raw_text)
        f.close()

        print 'Saving backup copy of Market data for %s to: %s' % (self.symbol, path)
        mf = file(market_path, 'w')
        mf.write(self.raw_market_text)
        mf.close()
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
                    parse_row.values.append(pq(col).text().strip().replace(',',''))

            r = pq(row)
            r.children('td').each(parse_col)

            row_dict = {parse_row.name: parse_row.values}
            self.json.update(row_dict)

        self.parsed_xml = pq(self.raw_text)
        self.parsed_xml.find('tr').each(parse_row)
        body_len = len(self.json)
        if body_len == 0 or body_len == 4:
            print 'NO DATA FOUND FOR: %s!' % self.symbol
            self.has_data = False
        else:
            self.has_data = True
        
        print 'Done parsing!'
        
    def market_data_to_json(self):
        self.market_json = self.raw_market_text
                          

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
