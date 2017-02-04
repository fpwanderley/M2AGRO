from django.contrib import admin

from models import Product, Harvest


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    # Displayed fields in the models list.
    list_display = ('id', 'name')

    # Fields used for editing.
    list_display_links = ('name',)


@admin.register(Harvest)
class HarvestAdmin(admin.ModelAdmin):

    # Displayed fields in the models list.
    list_display = ('id', 'name', 'initial_date', 'final_date')

    # Fields used for editing.
    list_display_links = ('name',)
