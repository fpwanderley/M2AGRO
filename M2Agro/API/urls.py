from django.conf.urls import url

from . import views

# /m2agro/api/
urlpatterns = [

    # List with all Products in DB.
    url(r'products/$', views.ProductList.as_view()),

    # GET, PUT e DELETE de Product.
    url(r'product/$', views.ProductDetail.as_view()),

    # List with all Harvests in DB.
    url(r'harvests/$', views.HarvestList.as_view()),

    # GET, PUT e DELETE de Harvest.
    url(r'harvest/$', views.HarvestDetail.as_view()),

    # List with all Services in DB.
    url(r'services/$', views.ServiceList.as_view()),

]
