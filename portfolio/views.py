from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

from .models import (
    PersonalInfo, Skill, Experience, Project,
    Education, Achievement, Contact, SiteSettings
)

def home(request):
    """Home page view"""
    try:
        personal_info = PersonalInfo.objects.filter(is_active=True).first()
        skills = Skill.objects.filter(is_active=True).order_by('-proficiency')
        experiences = Experience.objects.filter(is_active=True).order_by('-start_date')
        projects = Project.objects.filter(is_active=True).order_by('-created_at')
        education = Education.objects.filter(is_active=True).order_by('-start_date')
        achievements = Achievement.objects.filter(is_active=True).order_by('-year')
        site_settings = SiteSettings.objects.filter(is_active=True).first()
    except Exception as e:
        # Fallback to empty data if there's an error
        personal_info = None
        skills = []
        experiences = []
        projects = []
        education = []
        achievements = []
        site_settings = None

    context = {
        'personal_info': personal_info,
        'skills': skills,
        'experiences': experiences,
        'projects': projects,
        'education': education,
        'achievements': achievements,
        'site_settings': site_settings,
    }

    return render(request, 'portfolio/home.html', context)

def privacy_policy(request):
    """Privacy Policy page view"""
    return render(request, 'portfolio/privacy_policy.html')

@csrf_exempt
@require_http_methods(["POST"])
def contact_submit(request):
    """Handle contact form submission via AJAX"""
    try:
        data = json.loads(request.body)
        name = data.get('name', '').strip()
        email = data.get('email', '').strip()
        message = data.get('message', '').strip()

        # Validation
        if not all([name, email, message]):
            return JsonResponse({
                'success': False,
                'message': 'Please fill in all fields.'
            }, status=400)

        # Email validation
        if '@' not in email or '.' not in email:
            return JsonResponse({
                'success': False,
                'message': 'Please enter a valid email address.'
            }, status=400)

        # Save to database
        contact = Contact.objects.create(
            name=name,
            email=email,
            message=message
        )

        # Send email notification (if configured)
        if hasattr(settings, 'CONTACT_EMAIL') and settings.CONTACT_EMAIL:
            try:
                send_mail(
                    subject=f'New Contact Form Submission from {name}',
                    message=f"""
                    Name: {name}
                    Email: {email}
                    Message: {message}
                    """,
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    recipient_list=[settings.CONTACT_EMAIL],
                    fail_silently=True,
                )
            except Exception as e:
                # Log error but don't fail the request
                print(f"Email sending failed: {e}")

        return JsonResponse({
            'success': True,
            'message': 'Thank you for your message! I\'ll get back to you soon.'
        })

    except json.JSONDecodeError:
        return JsonResponse({
            'success': False,
            'message': 'Invalid request format.'
        }, status=400)
    except Exception as e:
        return JsonResponse({
            'success': False,
            'message': 'An error occurred. Please try again later.'
        }, status=500)

def project_detail(request, project_id):
    """Project detail page view"""
    try:
        project = Project.objects.get(id=project_id, is_active=True)
    except Project.DoesNotExist:
        return redirect('portfolio:home')

    context = {
        'project': project,
    }
    return render(request, 'portfolio/project_detail.html', context)

def experience_detail(request, experience_id):
    """Experience detail page view"""
    try:
        experience = Experience.objects.get(id=experience_id, is_active=True)
    except Experience.DoesNotExist:
        return redirect('portfolio:home')

    context = {
        'experience': experience,
    }
    return render(request, 'portfolio/experience_detail.html', context)
