# -*- coding: utf-8 -*-

from rest_framework import serializers

from models import Product, Harvest, Service, ServiceProduct

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


class ServiceProductSerializer(serializers.ModelSerializer):

    service = serializers.IntegerField(required=False,
                                       write_only=True)

    class Meta:
        model = ServiceProduct
        fields = ('id', 'product', 'service', 'quantity', 'total_cost')


class ServiceSerializer(serializers.ModelSerializer):

    service_products = ServiceProductSerializer(many=True)

    def update(self, instance, validated_data):
        """
            Creates a new Service and sets the DB dependencies.

        :param instance:
        :param validated_data: Dict with the obj values.
        :return: New Service obj.
        """

        service_products = validated_data.pop('service_products')

        service = Service.objects.create(**validated_data)

        for service_product in service_products:

            service_product['product'] = service_product['product'].pk
            prod_serializer = ServiceProductSerializer(ServiceProduct(), data=service_product)

            if prod_serializer.is_valid():
                prod_serializer.validated_data['service'] = service
                prod_obj = prod_serializer.save()

        return service

    class Meta:
        model = Service
        fields = ('id', 'harvest', 'name', 'initial_date', 'final_date', 'service_products')


