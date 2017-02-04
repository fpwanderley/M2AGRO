# -*- coding: utf-8 -*-

from rest_framework import serializers

from models import Product

"""
    Serializers for API use.
"""


class ProductListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name')
