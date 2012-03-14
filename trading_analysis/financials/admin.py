__author__ = 'adewinter'
from django.contrib import admin
from trading_analysis.financials.models import Company, StatementItem, MarketDataPoint

admin.site.register(Company)
admin.site.register(StatementItem)
admin.site.register(MarketDataPoint)