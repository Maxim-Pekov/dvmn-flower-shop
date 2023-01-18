from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import Truncator

from .models import Specialist, Flower, Bouquet, Courier, Category, Consultation, Order


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacation',)


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'description',)


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacation',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'time_at', 'time_finish')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer', 'address', 'phone', 'delievry_date')


