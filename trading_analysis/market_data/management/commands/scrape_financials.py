from django.core.management.base import BaseCommand
from finance_grabber import FinScraper
from django.conf import settings
from trading_analysis.financials.models import Company, StatementItem
from refreshMarketData import fillMarketData
import trading_analysis.financials.models as m
import os
from os.path import split as ssplit

class Command(BaseCommand):
    market_data_fname = '%s_market_data.html'
    p = ssplit(os.path.abspath(m.__file__))[0]
    p = ssplit(p)[0]
    p = ssplit(p)[0]
    mdata_path = os.path.join(p,'market_data',market_data_fname)


    def handle(self, *args, **options):
        """
        Pulls in the Financial data of a list of companies (given by the django settings variable FIN_COMPANY_LIST
        """
        self.debug = False
        companies = settings.FIN_COMPANY_LIST
        for company_ in companies:
            sym = company_[1]
            company = company_[0]
            print 'Getting info for [%s] %s' % (sym,company)
            f = FinScraper(sym).parse()
            f_json = f.json
            if not f.has_data:
                print 'No Financial Data for %s found!!' % sym
                continue
            c = Company.objects.get_or_create(name=company,ticker_symbol=sym)[0]
            try:
                years = f_json["Year"]

            except KeyError as e:
                print "Couldn't find 'Years' in Financials Data, skipping compnay! Company:%s" % sym
                print '%s, %s' % (e.message, e.args)
                continue
            for line_item in f_json.keys():

                for i, year in enumerate(years):
                    try:
                        if self.debug:
#                            print '%s => %s' % (line_item, f_json[line_item][i])
                            print 'Slug: %s' % line_item
                            print 'Value: %s' % f_json[line_item][i]
                            print 'Year: %s' % year
                            print 'Company: %s' % c
                        StatementItem.objects.get_or_create(slug=line_item, value=f_json[line_item][i], year=year, company=c)
                    except IndexError:
                        pass
        fillMarketData()
