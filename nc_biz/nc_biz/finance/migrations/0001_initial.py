# Generated by Django 2.0 on 2018-04-29 18:18

from decimal import Decimal
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tick', models.CharField(max_length=100)),
                ('close', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('opening', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('dayRng', models.CharField(max_length=100)),
                ('yrRng', models.CharField(max_length=100)),
                ('volume', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('avgVolume', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('cap', models.CharField(max_length=100)),
                ('yrEst', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('url', models.CharField(max_length=100)),
                ('bid', models.CharField(max_length=100)),
                ('ask', models.CharField(max_length=100)),
                ('eps', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('peRatio', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('forwardDividend', models.CharField(max_length=100)),
                ('beta', models.DecimalField(blank=True, decimal_places=2, default=Decimal('0'), max_digits=19, null=True)),
                ('name', models.CharField(max_length=100)),
                ('hq', models.CharField(max_length=100)),
                ('logo', models.CharField(max_length=100)),
                ('latLng', models.CharField(max_length=100)),
                ('site', models.CharField(max_length=100)),
                ('cat', models.CharField(max_length=100)),
            ],
        ),
    ]
