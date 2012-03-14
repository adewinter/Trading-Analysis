# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, HttpResponseNotAllowed, HttpResponseNotModified
from django.template import RequestContext
from django.core.management import call_command
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from trading_analysis.financials.models import Company, StatementItem, MarketDataPoint
import pprint
import datetime
from django.db.models import Avg
import logging
from django.conf import settings
import os

logger = logging.getLogger()
pp = pprint.PrettyPrinter(indent=4).pprint
def cleanString(s):
    ret = s
    hasOpenParen = s.__contains__('(')
    hasCloseParen = s.__contains__(')')
    if hasOpenParen and hasCloseParen:
        ret = s.replace('(','').replace(')','')
        ret = '-' + ret

    ret = ret.replace(',','')
    return ret

def convertToNumber(s):
    s = cleanString(s)
    if s.__contains__('.'):
        return float(s)
    else:
        return int(float(s))

def getStatementItem(slug,company,year):
    si = StatementItem.objects.filter(slug=slug, company=company, year=year)
    if si.count() > 0:
        return si[0].value
    else:
        return None

def getCurrencyItem(slug,company,year):
    si = getStatementItem(slug,company,year)
    if si:
        return convertToNumber(si)*1000
    else:
        return None

def getCompanyContext(companyQS):
    c = {}
    companies = companyQS
    for company in companies:
        logger.debug('Building Context for Company: %s...' % company.ticker_symbol)
        print 'Building Context for Company:%s...' % company.ticker_symbol
        name = company.name
        sym = company.ticker_symbol
        if (not name) or (not sym):
            continue
        assets = None
        debts = None
        cashflow = None
        avg_price = None
        years = None
        dps = None
        cc = []
        #do calc:
#        try:
        years = StatementItem.objects.filter(slug="Year", company=company)
        for year in years:
            y = convertToNumber(year.value.replace('y_',''))
            if not year or year == '':
                continue
            year_start = datetime.date(year=int(y),month=01,day=01)
            year_end = datetime.date(year=int(y),month=12,day=31)
            avg_price = MarketDataPoint.objects.filter(company=company,date__range=(year_start,year_end)).aggregate(Avg('Close'))["Close__avg"]
            asset = getCurrencyItem('Total Assets',company,y)
            deb = getCurrencyItem(slug='Total Liabilities', company=company, year=y)
            cash = getCurrencyItem(slug='Cash Ex Operations', company=company, year=y)
            year_end_month = StatementItem.objects.filter(slug__icontains='year end month', company=company, year=y)[0].value
            year_end_month = datetime.datetime.strptime(year_end_month,'%B').month

            shares = StatementItem.objects.filter(slug__icontains='Ordinary Shares in Issue', company=company, year=y)
            if shares.count() > 0:
                shares = shares[0].value
            else:
                shares = '0.001'
            shares = convertToNumber(shares)*1000
            shares = 1 if shares <= 0 else shares

            dps = getCurrencyItem(slug='Dividends Paid', company=company, year=y)
            dps = (dps*1.0)/shares
            if cash and asset and deb:
                value = (asset + cash - deb)
                share_val = (value/(shares*1.0)) + dps
                if share_val and avg_price:
                    delta = share_val - avg_price
                else:
                    delta = 0
            else:
                value = None
                share_val = None
                delta = None

            y_context = {
                "Cash" : cash,
                "Debt" : deb,
                "Assets" : asset,
                "Value" : value,
                "DPS" : dps,
                "SharesOutstanding" : shares,
                "ShareVal" : share_val,
                "YearEnd" : year_end_month,
                "AvgPrice" : avg_price,
                "Delta": delta,
            }
            cc.append((y, y_context))
        if years.count() > 0:
            start_year = int(years[0].value)
            start_year = datetime.date(start_year,01,01)
#            end_year = int(years[years.count()-1].value)
    #        end_year = datetime.date(end_year,12,31)
            end_year = datetime.date.today()
        else:
            start_year = datetime.date(2007,01,01)
            end_year = datetime.date.today()


        company.marketData = MarketDataPoint.objects.filter(company=company, date__range=(start_year,end_year)).order_by('date')
        c[company] = cc
#        except ObjectDoesNotExist as e:
#            print '[%s] Exception! %s, %s ' % (company.ticker_symbol, e, e.args)
#            c["Company Msg"] = e
#            raise e
##            raise e


        today = datetime.date.today()
        thieyearstart = datetime.date(today.year,01,01)
        avg_price = MarketDataPoint.objects.filter(company=company,date__range=(thieyearstart,today)).aggregate(Avg('Close'))["Close__avg"]
        company.avgpricethisyear = avg_price
    return c

def draw_companies(companies, request):
    """
    Draws a list of companies (valuation table plus plot)
    """
    companies_to_list = companies
    c = getCompanyContext(companies_to_list)
    context = {
        "company_data" : c,
    }
    return render_to_response("financials/Dashboard.html",context,context_instance=RequestContext(request))


def dashboard(request):
    """
    Shows a general view of all the companies in the DB (calculated value, market value, delta between those two values, etc)
    """
    symbol = request.GET.get("symbol",None)

    if symbol:
        symbol = symbol.split(',')
        company_to_list = Company.objects.filter(ticker_symbol__in=symbol)
        if symbol[0] == "ALL":
            company_to_list = Company.objects.all()
    else:
        company_to_list = Company.objects.filter(ticker_symbol='GRF')

    return draw_companies(company_to_list, request)

def interesting_companies(request):
    int_companies = ['GRF','HLM','AOO','AFT','AMA','ARH','ART','AEG','BAW','BNT','BRT','CPL','CRG','COL','CND','CNL','CVN','DTA','ELR','EMI','EQS','FPT','GPL','GRF','HCI','HLM','IRA','ING','KAP','KDV','MAS','MST','NCA','ORE','SAC','SBV','SAN','SKJ','SNU','SOH','SOV','SPA','TRE']
    companies = Company.objects.filter(ticker_symbol__in=int_companies)
    return draw_companies(companies, request)


def get_financial_report(request):
    if request.method == 'GET':
        symbol = request.GET.get('symbol',None)
        symbol = symbol.upper()
        fin_data_path = settings.FINANCE_DATA_PATH
	fin_data_path = os.path.join(fin_data_path,'%s_financial_data.html' % symbol)
        f = open(fin_data_path, 'r')
        lines = f.readlines()
        f.close()
        return HttpResponse(lines)
    else:
        return HttpReponse('Failed')
