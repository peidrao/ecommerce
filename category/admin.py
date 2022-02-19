from django.contrib import admin

from category.models import Category


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)}
    display_name = ('category_name', 'slug')


admin.site.register(Category, CategoryAdmin)
