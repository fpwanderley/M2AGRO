# -*- coding: utf-8 -*-

from rest_framework import serializers

from models import Product, Harvest

"""
    Serializers for API use.
"""


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name')


class HarvestListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Harvest
        fields = ('id', 'name', 'initial_date', 'final_date')
