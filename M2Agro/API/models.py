# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.db import models


class Product(models.Model):

    name = models.CharField(u"Nome do Produto",
                            max_length=100,
                            unique=True)

    average_cost = models.DecimalField(u"Custo Médio do Produto (R$)",
                                       max_digits=15,
                                       decimal_places=2,
                                       null=True,
                                       blank=True)

    def __str__(self):
        return self.name


class Harvest(models.Model):

    name = models.CharField(u"Nome da Colheita",
                            max_length=100)

    initial_date = models.DateField(verbose_name=u'Data Inicial da Colheita',
                                    editable=True)

    final_date = models.DateField(verbose_name=u'Data Final da Colheita',
                                  editable=True)

    def __str__(self):
        return self.name


class Service(models.Model):

    harvest = models.ForeignKey(Harvest, related_name="harvests")

    name = models.CharField(u"Nome do Serviço",
                            max_length=100)

    initial_date = models.DateField(verbose_name=u'Data Inicial do Serviço',
                                    editable=True)

    final_date = models.DateField(verbose_name=u'Data Final do Serviço',
                                  editable=True)


class ServiceProduct(models.Model):

    product = models.ForeignKey(Product, related_name="products")

    service = models.ForeignKey(Service, related_name="services")

    quantity = models.DecimalField(u"Quantidade do Produto no Serviço",
                                   max_digits=15,
                                   decimal_places=2,
                                   null=True,
                                   blank=True)

    total_cost = models.DecimalField(u"Custo Total do Produto no Serviço",
                                     max_digits=15,
                                     decimal_places=2,
                                     null=True,
                                     blank=True)
