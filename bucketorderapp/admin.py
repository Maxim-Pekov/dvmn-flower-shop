from django.contrib import admin
from django.utils.safestring import mark_safe
from django.utils.text import Truncator
from django.contrib.admin.options import TabularInline

from .models import Specialist, Flower, Bouquet, Courier, Category, Consultation, Order


def get_image_preview_markup(bouquet):
    return mark_safe(f'<img src="{bouquet.image.url}" height=200>')


class BouquetAdminInline(TabularInline):
    model = Bouquet
    fields = ('title', get_image_preview_markup, 'price')
    readonly_fields = (get_image_preview_markup,)

    extra = 0

    get_image_preview_markup.short_description = 'изображение'


@admin.register(Specialist)
class SpecialistAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacation',)


@admin.register(Flower)
class FlowerAdmin(admin.ModelAdmin):
    list_display = ('title',)


@admin.register(Bouquet)
class BouquetAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', get_image_preview_markup, 'description',)
    fields = ('title', 'price', get_image_preview_markup, 'image',)
    readonly_fields = (get_image_preview_markup,)
    sortable_by = ('price', 'title')
    list_filter = ('categories', 'price')
    ordering = ['price']

    get_image_preview_markup.short_description = 'Фото букета'

@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('name', 'vacation',)


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title',)
    inlines = [
        BouquetAdminInline,
    ]

@admin.register(Consultation)
class ConsultationAdmin(admin.ModelAdmin):
    list_display = ('customer', 'phone', 'time_at', 'time_finish')


def get_image2_preview_markup(order):
    return mark_safe(f'<img src="{order.bouquet.image.url}" height=200>')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = (get_image2_preview_markup, 'customer', 'address', 'phone',
    'delievry_date')


