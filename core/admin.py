from django.contrib import admin

from core.models import Students

# Register your models here.


@admin.register(Students)
class StudentsAdmin(admin.ModelAdmin):
    list_display = ['tt_number', 'full_name', 'gender', 'id_number', 'centre_code', 'centre_name', 'grade', 'trade_code', 'trade_name', 'test_series', 'result', 'photo_link']