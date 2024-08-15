from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.job_list, name='job_list'),  # Job list view
    path('job/<int:pk>/', views.job_detail, name='job_detail'),  # Job detail view
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Login view
    path('logout/', auth_views.LogoutView.as_view(next_page='job_list'), name='logout'),  # Logout view with redirect
    path('register/', views.register, name='register'),  # User registration view
    path('search/', views.search_jobs, name='search_jobs'),  # Job search view
    path('about/', views.about, name='about'),  # About page view
    path('contact/', views.contact, name='contact'),  # Contact page view
    path('dashboard/', views.dashboard, name='dashboard'),  # Dashboard view
    path('job/create/', views.job_create, name='job_create'),  # Create job view
    path('job/<int:pk>/edit/', views.job_update, name='job_update'),  # Update job view
    path('job/<int:pk>/delete/', views.job_delete, name='job_delete'),  # Delete job view
    path('about/', views.about, name='about'),
 
]
