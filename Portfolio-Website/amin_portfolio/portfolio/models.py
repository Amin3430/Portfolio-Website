
from django.db import models
from django.utils import timezone

class Project(models.Model):
    CATEGORY_CHOICES = [
        ('web', 'Web Development'),
        ('api', 'API Development'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=300)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='web')
    github_link = models.URLField(blank=True, null=True)
    demo_link = models.URLField(blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

class Skill(models.Model):
    SKILL_CATEGORIES = [
        ('language', 'Programming Languages'),
        ('framework', 'Frameworks & APIs'),
        ('database', 'Databases'),
        ('tool', 'Development Tools'),
        ('soft', 'Soft Skills'),
    ]
    
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    proficiency = models.IntegerField(default=50, help_text="Proficiency level (1-100)")

    def __str__(self):
        return self.name

class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    description = models.TextField()
    location = models.CharField(max_length=200)
    is_current = models.BooleanField(default=False)

    class Meta:
        ordering = ['-start_date']

    def __str__(self):
        return f"{self.position} at {self.company}"

class Certification(models.Model):
    name = models.CharField(max_length=200)
    issuer = models.CharField(max_length=200)
    date_earned = models.DateField()
    credential_url = models.URLField(blank=True, null=True)

    class Meta:
        ordering = ['-date_earned']

    def __str__(self):
        return f"{self.name} - {self.issuer}"