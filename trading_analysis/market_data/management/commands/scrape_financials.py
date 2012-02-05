__author__ = 'adewinter'
from django.core.management.base import BaseCommand
from finance_grabber import FinScraper
from django.conf import settings



class Command(BaseCommand):
    """
    Pulls in the Financial data of a list of companies (given by the django settings variable FIN_COMPANY_LIST
    """
    def handle(self, *args, **options):
        f = FinScraper(None)
        