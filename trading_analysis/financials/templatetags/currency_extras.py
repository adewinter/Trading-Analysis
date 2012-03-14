from django.contrib.humanize.templatetags.humanize import intcomma
from django import template
import time
register = template.Library()

def currency_rand(zar):
    if not zar:
        return "None"
    zar = float(zar)
    return "R%s%s" % (intcomma(int(zar)), ("%0.2f" % zar)[-3:])

def currency_rand_round(zar):
    if not zar:
        return "None"
    zar = float(zar)
    return "R%s" % (intcomma(int(zar)))

def currency_rand_without_symbol(zar):
    return currency_rand(zar).strip('R')

def epoch(value):
    try:
        return int(time.mktime(value.timetuple())*1000)
    except AttributeError:
        return ''

register.filter('currency_rand',currency_rand)
register.filter('currency_rand_round',currency_rand_round)
register.filter('currency_rand_without_symbol', currency_rand_without_symbol)
register.filter('epoch',epoch)