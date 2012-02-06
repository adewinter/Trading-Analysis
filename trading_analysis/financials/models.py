from django.db import models

class Company(models.Model):
    """
        Describes a Company that can be traded
    """
    name = models.CharField(max_length=255)
    ticker_symbol = models.CharField(max_length=10)
    description = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return "Company: [%s] %s" % (self.ticker_symbol, self.name)



class StatementItem(models.Model):
    """
        A line item from the company's financial statemnt
    """
    slug = models.CharField(max_length=255, help_text="Item name, e.g. 'Assets' or 'EPS-Bottom Line'")
    year = models.CharField(max_length=4, help_text="The year that this line item refers to")
    value = models.CharField(max_length=255, help_text="The value of this line item, for the specified year")
    company = models.ForeignKey(Company)

    def __unicode__(self):
        return "%s:%s :: %s, %s" % (self.slug, self.value, self.company.ticker_symbol, self.year)