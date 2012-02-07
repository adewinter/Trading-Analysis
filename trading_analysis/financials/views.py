# Create your views here.
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect, render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponseForbidden, HttpResponse, HttpResponseNotAllowed, HttpResponseNotModified
from django.template import RequestContext
from django.core.management import call_command
from django.contrib.auth.views import login as django_login
from django.contrib.auth.views import logout as django_logout
from trading_analysis.financials.models import Company, StatementItem

def convertToInt(s):
    ret = s
    hasOpenParen = s.__contains__('(')
    hasCloseParen = s.__contains__(')')
    if hasOpenParen and hasCloseParen:
        ret = s.replace('(','').replace(')','')
        ret = int(ret)
        ret = (ret * -1)
    else:
        ret = int(s)
    return ret

def dashboard(request):
    c = {}
    companies = Company.objects.all()
    for company in companies:
        name = company.name
        sym = company.ticker_symbol

        assets = None
        debts = None
        cashflow = None
        years = None
        cc = {}
        #do calc:
        try:
            years = StatementItem.objects.filter(slug="Year", company=company)
            for year in years:
                y = year.value.replace('y_','')
                asset = StatementItem.objects.get(slug='Total Assets', company=company, year=y).value
                asset = convertToInt(asset)*1000
                deb = StatementItem.objects.get(slug='Total Liabilities', company=company, year=y).value
                deb = convertToInt(deb)*1000
                cash = StatementItem.objects.get(slug='Cash Ex Operations', company=company, year=y).value
                cash = convertToInt(cash)*1000
                shares = StatementItem.objects.get(slug__icontains='Nr of Ordinary Shares in Issue', company=company, year=y).value
                shares = convertToInt(shares)*1000
                value = (asset + cash - deb)
                share_val = value/(shares*1.0)

                y_context = {
                    "Cash" : cash,
                    "Debt" : deb,
                    "Assets" : asset,
                    "Value" : value,
                    "ShareVal" : share_val
                }
                cc['y_%s' % y ] = y_context
        except ObjectDoesNotExist as e:
            print 'Exception! %s ' % e
            c["Company Msg"] = e
            continue

        c[company] = cc

    context = {
        "company_data" : c
    }

    return render_to_response("financials/Dashboard.html",context,context_instance=RequestContext(request))

#    pass