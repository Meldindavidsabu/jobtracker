# jobs/admin.py

from django.contrib import admin
from .models import Company, Job

# Customizing the Admin Interface
admin.site.site_header = "Your Job Tracker - Admin"
admin.site.site_title = "Your Job Tracker"
admin.site.index_title = "Admin Dashboard"

class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    search_fields = ('name', 'location')

class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'application_date', 'status')
    list_filter = ('company', 'status')
    search_fields = ('title', 'description')

admin.site.register(Company, CompanyAdmin)
admin.site.register(Job, JobAdmin)
