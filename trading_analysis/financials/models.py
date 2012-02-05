from django.db import models

class Company(models.Model):
    """
        Describes a Company that can be traded
    """
    name = models.CharField(max_length=255)
    ticker_symbol = models.CharField(max_length=10)
    description = models.TextField()



class StatementItem(models.Model):
    """
        A line item from the company's financial statemnt
    """
    slug = models.CharField(max_length=255, help_text="Item name, e.g. 'Assets' or 'EPS-Bottom Line'")
    year = models.CharField(max_length=4, help_text="The year that this line item refers to")
    value = models.CharField(max_lenght=255, help_text="The value of this line item, for the specified year")
    company = models.ForeignKey(Company)


