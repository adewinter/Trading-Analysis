import datetime
from django.core.management.base import BaseCommand
from trading_analysis.financials.models import Company, MarketDataPoint
import trading_analysis.financials.models as m
import os
from os.path import split as ssplit
import json
import sys


class Command(BaseCommand):
    def handle(self, *args, **options):
        fillMarketData()

def fillMarketData():
    market_data_fname = '%s_market_data.html'
    p = os.path.abspath(m.__file__)
    p = ssplit(p)[0]
    p = ssplit(p)[0]
    p = ssplit(p)[0]
    mdata_path = os.path.join(p,'market_data',market_data_fname)

    companies = Company.objects.all()
    for company in companies:
        print 'Populating Market data for Company: %s' % company.ticker_symbol
        f = open(mdata_path % company.ticker_symbol)
        lines = ''
        for line in f.readlines():
            lines += line

        json_data = json.loads(lines)
        data_points = json_data["Object"]
        num_points_file = len(data_points)
        num_points_db = MarketDataPoint.objects.filter(company=company).count()
        print 'Number of Market Data Points in DB: %s, Number of Market Data Points in File: %s' % (num_points_db, num_points_file)
        if num_points_file == num_points_db:
            print 'Same number of data points in file as in DB. Skipping this company! [%s]' % company.ticker_symbol
            continue
        print '[%s] Loading %s points...' % (company.ticker_symbol, num_points_file)
        for d in data_points:
            AfrikaansInstrumentName = d["AfrikaansInstrumentName"]
            Change = str(["Change"])
            Close = str(d["Close"])
            DateStampFormatted = d["DateStampFormatted"]
            date = datetime.datetime.strptime(DateStampFormatted, '%d%m%Y')
            High = str(d["High"])
            InstrumentIdentifier = d["InstrumentIdentifier"]
            InstrumentName = d["InstrumentName"]
            Low = str(d["Low"])
            Movement = d["Movement"]
            Open = str(d["Open"])
            PercentageChange = d["PercentageChange"]
            Volume = d["Volume"]
            (md, created) = MarketDataPoint.objects.get_or_create(
                                            company = company,
                                            AfrikaansInstrumentName = AfrikaansInstrumentName,
                                            Change = Change,
                                            Close = Close,
                                            date = date,
                                            High = High,
                                            InstrumentIdentifier = InstrumentIdentifier,
                                            InstrumentName = InstrumentName,
                                            Low = Low,
                                            Movement = Movement,
                                            Open = Open,
                                            PercentageChange = PercentageChange,
                                            Volume = Volume
            )
            sys.stdout.write('N' if created else '.')


        print '\nDone loading data points for %s!' % company.ticker_symbol
