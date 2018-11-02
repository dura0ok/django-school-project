from django.contrib import admin

# Register your models here.
from .models import Menu, Page


admin.site.register(Page)


class AdminMenus(admin.ModelAdmin):
    admin.site.register(Menu)
    ordering = ('-sort',)