
from django.contrib import admin
from .models import Project, Skill, Experience, Certification

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'is_featured', 'created_date']
    list_filter = ['category', 'is_featured', 'created_date']
    search_fields = ['title', 'description', 'technologies']
    list_editable = ['is_featured']

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'proficiency']
    list_filter = ['category']
    search_fields = ['name']

@admin.register(Experience)
class ExperienceAdmin(admin.ModelAdmin):
    list_display = ['position', 'company', 'start_date', 'end_date', 'is_current']
    list_filter = ['is_current', 'start_date']
    search_fields = ['company', 'position']

@admin.register(Certification)
class CertificationAdmin(admin.ModelAdmin):
    list_display = ['name', 'issuer', 'date_earned']
    list_filter = ['date_earned']
    search_fields = ['name', 'issuer']