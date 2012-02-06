__author__ = 'adewinter'
from django.contrib import admin
from trading_analysis.financials.models import Company, StatementItem

admin.site.register(Company)
admin.site.register(StatementItem)