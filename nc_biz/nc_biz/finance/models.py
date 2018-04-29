from django.db import models
from decimal import Decimal

# Create your models here.

class Company(models.Model):
    tick = models.CharField(max_length=100)
    close = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    opening = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    dayRng = models.CharField(max_length=100)
    yrRng = models.CharField(max_length=100)
    volume = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    avgVolume = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    cap = models.CharField(max_length=100)
    yrEst = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    url= models.CharField(max_length=100)
    bid = models.CharField(max_length=100)
    ask = models.CharField(max_length=100)
    eps = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    peRatio = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    forwardDividend = models.CharField(max_length=100)
    beta = models.DecimalField(max_digits=19, decimal_places=2, default=Decimal(0.0000), blank=True, null=True)
    name = models.CharField(max_length=100)
    hq = models.CharField(max_length=100)
    logo = models.CharField(max_length=100)
    latLng = models.CharField(max_length=100)
    site = models.CharField(max_length=100)
    cat = models.CharField(max_length=100)

    # class Meta:
    #     ordering = ('name',)

    def __str__(self):
        return U'%s' %(self.tick)

    def to_json(self):
        return{
            "tick": self.tick,
            "close": self.close,
            "opening": self.opening,
            "dayRng": self.dayRng,
            "yrRng": self.yrRng,
            "volume": self.volume,
            "avgVolume": self.avgVolume,
            "cap": self.cap,
            "yrEst": self.yrEst,
            "url": self.url,
            "bid": self.bid,
            "ask": self.ask,
            "eps": self.eps,
            "peRatio": self.peRatio,
            "forwardDividend": self.forwardDividend,
            "beta": self.beta,
            "name": self.name,
            "hq": self.hq,
            "site": self.site,
            "logo": self.logo,
            "latLng": self.latLng,
            "cat": self.cat,
        }
