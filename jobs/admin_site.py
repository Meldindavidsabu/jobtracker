from django.contrib.admin import AdminSite

class MyAdminSite(AdminSite):
    site_header = "Your Job Tracker"
    site_title = "Your Job Tracker - Admin"
    index_title = "Welcome to Your Job Tracker Admin"

admin_site = MyAdminSite()
