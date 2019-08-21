from django.contrib import admin
from .models import Page

# Register your models here.
class PageAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'orden')

    class Media:
        css = {
            'all': ('custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
