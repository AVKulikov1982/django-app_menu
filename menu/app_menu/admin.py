from django.contrib import admin
from app_menu.models import MenuCategory
from mptt.admin import MPTTModelAdmin


@admin.register(MenuCategory)
class MenuCategoryAdmin(MPTTModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
