from django.contrib import admin

from dogs.models import Category, Dog


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', )
    list_filter = ('category',)