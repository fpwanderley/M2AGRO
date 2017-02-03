from django.conf.urls import url

from . import views

# /m2agro/api/
urlpatterns = [

    # List with all Products in DB.
    url(r'products/$', views.ProductList.as_view()),

    # GET e PUT de ComplexProductionOrderDetail.
    url(r'product/$', views.ProductDetail.as_view()),

]
