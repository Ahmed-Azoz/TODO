from django.contrib import admin
from .models import Todo #اسم الكلاس بتاع الموديل

class TodoAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)

admin.site.register(Todo, TodoAdmin)
