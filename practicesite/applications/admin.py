from django.contrib import admin
from applications.models import Application

# Register your models here.
# admin.site.register(Application)

@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
	list_display = ('company', 'position', 'status', 'date_applied', 'deadline', 'owner')
	list_filter = ('status', 'date_applied')