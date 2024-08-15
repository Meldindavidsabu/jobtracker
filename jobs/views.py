from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.contrib import messages
from django.db.models import Count
from .forms import JobForm, UserRegistrationForm
from .models import Job, Company

@login_required
def job_list(request):
    jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/job_list.html', {'jobs': jobs})

@login_required
def job_detail(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    return render(request, 'jobs/job_detail.html', {'job': job})

@login_required
def job_create(request):
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)  
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('job_list')
    else:
        form = JobForm()
    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_update(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES, instance=job)  
        if form.is_valid():
            job = form.save(commit=False)
            job.save()
            return redirect('job_list')
    else:
        form = JobForm(instance=job)
    return render(request, 'jobs/job_form.html', {'form': form})

@login_required
def job_delete(request, pk):
    job = get_object_or_404(Job, pk=pk, user=request.user)
    if request.method == 'POST':
        job.delete()
        return redirect('job_list')
    return render(request, 'jobs/job_confirm_delete.html', {'job': job})

@login_required
def search_jobs(request):
    query = request.GET.get('q', '')
    if query:
        jobs = Job.objects.filter(title__icontains=query, user=request.user)
    else:
        jobs = Job.objects.filter(user=request.user)
    return render(request, 'jobs/search_results.html', {'jobs': jobs, 'query': query})

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            
            # Send welcome email
            subject = 'Welcome to Your Job Tracker'
            message = f'Dear {username},\n\nThank you for registering at Your Job Tracker. We are excited to have you on board!\n\nBest regards,\nYour Job Tracker Team'
            send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])
            
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def dashboard(request):
    status_counts = Job.objects.filter(user=request.user).values('status').annotate(total=Count('status'))
    context = {
        'status_counts': status_counts,
    }
    return render(request, 'jobs/dashboard.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'jobs/contact.html')
