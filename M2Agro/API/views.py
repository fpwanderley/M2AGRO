# -*- coding: utf-8 -*-

from django.db import transaction

from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework import permissions, status
from rest_framework.authentication import SessionAuthentication
from rest_framework.response import Response

from models import Product, Harvest
from serializers import ProductListSerializer, HarvestListSerializer


class CsrfExemptSessionAuthentication(SessionAuthentication):
    """
        Class used for exempting CSRT authentication. Explanation in the following link:

    http://stackoverflow.com/questions/30871033/django-rest-framework-remove-csrf
    """

    def enforce_csrf(self, request):
        return  # To not perform the csrf check previously happening


class ProductList(APIView):

    """
    Handles operations for a list of a Product.

    URL: /m2agro/api/products
    """

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @transaction.atomic
    def get(self, request, format=None):
        """
            Returns a Product list.

        Returns:
            Product list.
        """

        products = Product.objects.all()

        serializer = ProductListSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        """
            Creates a new Product.

        Args:
            request.data:
                'name': Product.name

        Returns:
            {
                'id': Product.id,
                'name' : Product.name
            }
        """

        # Serializes the Product obj to be created.
        serializer = ProductListSerializer(Product(), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductDetail(APIView):

    """
        Handles operations for a single Product instance.

        URL: /m2agro/api/product?<id>
    """

    permission_classes = (permissions.AllowAny,)

    authentication_classes = (CsrfExemptSessionAuthentication,)

    @transaction.atomic
    def get(self, request):
        """
            Returns a Product.

        args:
            request.query_params:
                'id': Product.id

        Returns:
            {
                'id': Product.id,
                'name' : Product.name
            }
        """

        id = request.query_params.get('id')

        product = get_object_or_404(Product, id=id)

        serializer = ProductListSerializer(product, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def put(self, request):
        """
            Edits a Product.

        args:
            request.query_params:
                'id': Product.id

            request.data:
                'name': Product.name

        Returns:
            {
                'id': Product.id,
                'name' : Product.name
            }
        """

        id = request.query_params.get('id')
        product = get_object_or_404(Product, id=id)

        serializer = ProductListSerializer(product, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request):
        """

            Deletes a Product.

        Args:
            request.query_params:
                'id': Product.id

        Returns:
            HTTP 204 if Product is deleted successfully.
        """

        id = request.query_params.get('id')
        product = get_object_or_404(Product, pk=id)

        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HarvestList(APIView):

    """
    Handles operations for a list of a Harvest.

    URL: /m2agro/api/harvests
    """

    permission_classes = (permissions.AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)

    @transaction.atomic
    def get(self, request, format=None):
        """
            Returns a Harvest list.

        Returns:
            Harvest list.
        """

        products = Harvest.objects.all()

        serializer = HarvestListSerializer(products, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def post(self, request):
        """
            Creates a new Harvest.

        PS: The DateFields 'initial_date' and 'final_date' must
        obey the following formatting: '<day>/<month>/<year>'

        Args:
            request.data:
                'name': Harvest.name
                'start_date': Harvest.initial_date
                'final_date': Harvest.final_date

        Returns:
            {
                'id': Harvest.id
                'name': Harvest.name
                'start_date': Harvest.initial_date
                'final_date': Harvest.final_date
            }
        """

        # Serializes the Harvest obj to be created.
        serializer = HarvestListSerializer(Harvest(), data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HarvestDetail(APIView):

    """
        Handles operations for a single Harvest instance.

        URL: /m2agro/api/harvest?<id>
    """

    permission_classes = (permissions.AllowAny,)

    authentication_classes = (CsrfExemptSessionAuthentication,)

    @transaction.atomic
    def get(self, request):
        """
            Returns a Harvest.

        args:
            request.query_params:
                'id': Harvest.id

        Returns:
            {
                'id': Harvest.id,
                'name' : Harvest.name
                'start_date': Harvest.initial_date
                'final_date': Harvest.final_date
            }
        """

        id = request.query_params.get('id')

        harvest = get_object_or_404(Harvest, id=id)

        serializer = HarvestListSerializer(harvest, many=False)

        return Response(serializer.data, status=status.HTTP_200_OK)

    @transaction.atomic
    def put(self, request):
        """
            Edits a Harvest.

        args:
            request.query_params:
                'id': Harvest.id

            request.data:
                'name': Harvest.name
                'start_date': Harvest.initial_date
                'final_date': Harvest.final_date

        Returns:
            {
                'id': Harvest.id,
                'name' : Harvest.name
                'start_date': Harvest.initial_date
                'final_date': Harvest.final_date
            }
        """

        id = request.query_params.get('id')
        harvest = get_object_or_404(Harvest, id=id)

        serializer = HarvestListSerializer(harvest, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @transaction.atomic
    def delete(self, request):
        """
            Deletes a Harvest.

        Args:
            request.query_params:
                'id': Harvest.id

        Returns:
            HTTP 204 if Harvest is deleted successfully.
        """

        id = request.query_params.get('id')
        harvest = get_object_or_404(Harvest, pk=id)

        harvest.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
