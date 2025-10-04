from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ['id','user','title','discription','status','created_at','updated_at']
    list_filter = ['status','title']
    search_fields = ['user','title']
    list_display_links = ['id','title']
admin.site.register(Task,TaskAdmin)
