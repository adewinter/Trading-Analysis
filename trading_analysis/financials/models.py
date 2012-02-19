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


class MarketDataPoint(models.Model):
    company = models.ForeignKey(Company)
    AfrikaansInstrumentName = models.CharField(max_length=100, null=True, blank=True)
    Change = models.CharField(max_length=10, null=True, blank=True)
    Close = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    date = models.DateField()
    High = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    InstrumentIdentifier = models.CharField(max_length=100, null=True, blank=True)
    InstrumentName = models.CharField(max_length=100, null=True, blank=True)
    Low = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    Movement = models.CharField(max_length=100, null=True, blank=True)
    Open = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    PercentageChange = models.CharField(max_length=100, null=True, blank=True)
    Volume = models.CharField(max_length=100, null=True, blank=True)

