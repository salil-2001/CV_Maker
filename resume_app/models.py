from django.db import models

class ResumeTemplate(models.Model):
    name = models.CharField(max_length=100)
    # Add fields for template customization (e.g., layout, fonts, styles)

class Resume(models.Model):
    template = models.ForeignKey(ResumeTemplate, on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    Position=models.CharField(max_length=50)
    contact=models.IntegerField()
    email=models.EmailField()
    address=models.TextField()
    about=models.TextField()

class Qualifications(models.Model):
    degree=models.CharField(max_length=100)
    college=models.CharField(max_length=100)
    year=models.DateField()
    course=models.CharField(max_length=100)
    institute=models.CharField(max_length=100)
    description=models.TextField()

class Experiance(models.Model):
    companyname=models.CharField(max_length=200)
    position=models.CharField(max_length=300)
    startdate=models.DateField()
    enddate=models.DateField()
    projects=models.CharField(max_length=50)
    project_discription=models.TextField()
    responsibilities=models.TextField()
    jobdescription=models.TextField()



