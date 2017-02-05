# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from datetime import datetime

from django.db import models

from exceptions import InvalidMonthORYear
from utils import is_valid_month, is_valid_year


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

    @classmethod
    def calculate_average_cost(cls, reference_month=None, reference_year=None, commit=True):
        """
            Calculates de average cost for the given Product.

        OBS 1: If reference_month==None or reference_year==None, the month before will be chosen.
        OBS 2: If reference_month is not valid, an Exception will be raised.

        :param reference_month: Integer among 1 and 12 for chosing the reference month.
        :param reference_year: Integer among 1900 and 2030 for chosing the reference year.
        :param commit: Boolean which determines if the 'average_cost' field has to be updated.

        :return: List of updated Products.
        """

        # Choose the month before.
        if reference_month is None or reference_year is None:
            now = datetime.now()
            reference_month = now.month
            reference_year = now.year

            if reference_month == 1:
                reference_year -= 1
                reference_month = 12

            else:
                reference_month -= 1

        # Calculates the average cost if the reference_month and reference_year is valid.
        if is_valid_month(reference_month) and is_valid_year(reference_year):

            # Gets all Services happening during the given month.
            ongoing_services = Service.get_ongoing_services(month=reference_month,
                                                            year=reference_year)

            # Gets the ServiceProducts of all these Services.
            service_products = ServiceProduct.objects.filter(service__in=ongoing_services)

            # Gets the distinct Products of all theses ServiceProducts.
            products = cls.objects.filter(service_products__in=service_products).distinct()

            # Calculates the average cost for each involved Product.
            changed_products = []
            for product in products:

                # Gets all ServiceProducts with this Products.
                prod_service_products = service_products.filter(product=product)

                # Calculates the total cost and total quantity.
                total_cost = sum([prod.total_cost for prod in prod_service_products])
                total_quantity = sum([prod.quantity for prod in prod_service_products])

                # Calculates the Product's average cost.
                if total_quantity != 0.0:
                    prod_average_cost = total_cost/total_quantity
                else:
                    prod_average_cost = 0.0

                product.average_cost = prod_average_cost
                changed_products.append(product)

                # Updates de DB if commit==True.
                if commit:
                    product.save()

            return changed_products

        # Raises an Exception for invalid values for month or year.
        else:
            raise InvalidMonthORYear()


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

    harvest = models.ForeignKey(Harvest,
                                verbose_name='Colheita',
                                related_name="harvests")

    name = models.CharField(verbose_name="Nome do Serviço",
                            max_length=100)

    initial_date = models.DateField(verbose_name=u'Data Inicial do Serviço',
                                    editable=True)

    final_date = models.DateField(verbose_name=u'Data Final do Serviço',
                                  editable=True)

    def __str__(self):
        return self.name

    @classmethod
    def get_ongoing_services(cls, month, year):
        """
            Returns all Services happening on a given month and year.

        :param month: Integer between 1 and 12.
        :param year: Integet between 1990 and 2050.
        :return: Service QuerySet.
        """

        services = Service.objects.filter(initial_date__year__lte=year,
                                          final_date__year__gte=year,
                                          initial_date__month__lte=month,
                                          final_date__month__gte=month)

        return services

    @property
    def total_cost(self):
        """
            Returns the sum of total_costs of all related ServiceProduct objs.

        :return: Float
        """

        return sum([prod.total_cost for prod in self.service_products.all()])


class ServiceProduct(models.Model):

    product = models.ForeignKey(Product, related_name="service_products")

    service = models.ForeignKey(Service, related_name="service_products")

    quantity = models.DecimalField(u"Quantidade do Produto no Serviço (Kg)",
                                   max_digits=15,
                                   decimal_places=2,
                                   null=True,
                                   blank=True)

    total_cost = models.DecimalField(u"Custo Total do Produto no Serviço (R$)",
                                     max_digits=15,
                                     decimal_places=2,
                                     null=True,
                                     blank=True)

    def __str__(self):
        return ('{product} em {service}').format(product=self.product.name,
                                                 service=self.service.name)
