__author__ = 'adewinter'
from django.core.management.base import BaseCommand
from finance_grabber import FinScraper
from django.conf import settings
from trading_analysis.financials.models import Company, StatementItem



class Command(BaseCommand):
    """
    Pulls in the Financial data of a list of companies (given by the django settings variable FIN_COMPANY_LIST
    """
    def handle(self, *args, **options):
        self.debug = True
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
            years = f_json["Year"]

            for line_item in f_json.keys():
                for i, year in enumerate(years):
                    try:
                        if self.debug:
#                            print '%s => %s' % (line_item, f_json[line_item][i])
                            print 'Slug: %s' % line_item
                            print 'Value: %s' % f_json[line_item][i]
                            print 'Year: %s' % year
                            print 'Company: %s' % (c)
                        StatementItem.objects.get_or_create(slug=line_item, value=f_json[line_item][i], year=year, company=c)
                    except IndexError:
                        pass