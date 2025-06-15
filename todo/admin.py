from django.contrib import admin
from todo.models import Task
@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed','created_at','updated_at','due_date')
    search_fields = ('title', 'description')
    list_filter = ('completed', 'created_at')
# Register your models here.
