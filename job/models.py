from django.db import models


from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


JOB_NATURES = (
    ('Full Time', 'Full Time'),
    ('Part Time', 'Part Time'),
    ('Remote', 'Remote'),
    ('Freelance', 'Freelance'),
)

class Job(models.Model):
    user = models.ForeignKey(User, related_name='job_author', on_delete=models.SET_NULL, null=True )
    category = models.ForeignKey('Category', related_name='job_category', on_delete=models.SET_NULL, null=True )
    
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='jobs')
    salary = models.IntegerField()
    location = models.CharField(max_length=150)
    posted_at = models.DateField(default=timezone.now)
    application_at = models.DateField()
    vacancy = models.CharField(max_length=10)
    job_nature = models.CharField(max_length=20, choices=JOB_NATURES)
    description = models.CharField(max_length=3000)
    experience_years = models.IntegerField()
    
    
class Company(models.Model):
    user = models.ForeignKey(User, related_name='company_author', on_delete=models.SET_NULL, null=True )
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=3000)
    website = models.CharField(max_length=150)
    email = models.EmailField(max_length=100)
    
class Category(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField(upload_to='categories')