import imp
from django.contrib import admin
from .models import Blog , Category , Comment

class admin_panel_setting_comment(admin.ModelAdmin):
    list_display = ('blog','Full_name','massage','is_active')
    list_editable = ('is_active',)
admin.site.register(Blog)
admin.site.register(Category)
admin.site.register(Comment,admin_panel_setting_comment)