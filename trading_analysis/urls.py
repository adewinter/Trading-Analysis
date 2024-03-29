from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'trading_analysis.financials.views.dashboard', name='home'),
    url(r'^interesting/$', 'trading_analysis.financials.views.interesting_companies', name='home'),
    url(r'^report/$', 'trading_analysis.financials.views.get_financial_report', name='fin_report'),
    # url(r'^trading_analysis/', include('trading_analysis.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
