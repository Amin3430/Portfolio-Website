from django.shortcuts import render
from django.http import HttpResponse
from .models import Project, Skill, Experience, Certification

def home(request):
    """Main portfolio page view"""
    
    # Get featured projects
    featured_projects = Project.objects.filter(is_featured=True)[:3]
    
    # Get all projects
    all_projects = Project.objects.all()[:6]
    
    # Get skills grouped by category
    skills = {
        'languages': Skill.objects.filter(category='language'),
        'frameworks': Skill.objects.filter(category='framework'),
        'databases': Skill.objects.filter(category='database'),
        'tools': Skill.objects.filter(category='tool'),
        'soft_skills': Skill.objects.filter(category='soft'),
    }
    
    # Get recent experience
    experiences = Experience.objects.all()[:3]
    
    # Get certifications
    certifications = Certification.objects.all()[:5]
    
    context = {
        'featured_projects': featured_projects,
        'all_projects': all_projects,
        'skills': skills,
        'experiences': experiences,
        'certifications': certifications,
    }
    
    return render(request, 'home.html', context)

def project_detail(request, project_id):
    """Project detail view"""
    try:
        project = Project.objects.get(id=project_id)
        context = {'project': project}
        return render(request, 'project_detail.html', context)
    except Project.DoesNotExist:
        return HttpResponse("Project not found", status=404)