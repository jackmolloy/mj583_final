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


    # class Meta:
    #     ordering = ('name',)

    def __str__(self):
        return U'%s' %(self.tick)


# class Close(models.Model):
#     name = models.CharField(max_length=100)
#
#     class Meta:
#         ordering = ('name',)
#
#     def __str__(self):
#         return self.name
