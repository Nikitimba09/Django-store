from django.contrib import admin

from products.models import ProductCategory, Product, Basket

admin.site.register(ProductCategory)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # Отображение параметров модели
    fields = ('name', 'description', 'price', 'quantity', 'image', 'category')  # Изменение параметров внутри объекта БД
    readonly_fields = ('description',)  # Параметры только для чтения
    search_fields = ('name',)  # Поиск объектов по параметру "name"
    ordering = ('name',)  # Сортировка в алфавитном порядке, если поставить "-name" то в обратном порядке


class BasketAdmin(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0