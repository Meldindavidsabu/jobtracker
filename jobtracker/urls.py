# jobtracker/urls.py

from django.contrib import admin
from django.urls import path, include
from jobs.views import search_jobs

urlpatterns = [
    path('', include('jobs.urls')),  
    path('admin/', admin.site.urls),  # Django admin route
    path('accounts/', include('django.contrib.auth.urls')),  # Authentication routes
    path('search/', search_jobs, name='search_jobs'),  # Search functionality
]
