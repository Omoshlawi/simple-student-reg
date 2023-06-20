from django.contrib import admin

from core.models import Students

# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['tt_number', 'results','verified', 'image']