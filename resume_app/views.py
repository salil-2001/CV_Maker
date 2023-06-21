from django.shortcuts import render, redirect
from .models import ResumeTemplate, Resume, Qualifications,Experiance

def choose_template(request):
    templates = ResumeTemplate.objects.all()
    
    return render(request, 'choose_template.html', {'templates': templates})

def create_resume(request, template_id):
    template = ResumeTemplate.objects.get(id=template_id)
    if request.method == 'POST':
        resume = Resume(template=template)
        resume.name = request.POST['name']
        resume.position = request.POST['position']
        resume.contact = request.POST['contact']
        resume.email = request.POST['email']
        resume.address = request.POST['address']
        resume.about = request.POST['about']
        resume.save()

        return redirect('add_qualifications', resume_id=resume.id)

    return render(request, 'create_resume.html', {'template': template})

def add_qualifications(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':
        qualification = Qualifications(
            degree=request.POST['degree'],
            college=request.POST['college'],
            year=request.POST['year'],
            course=request.POST['course'],
            institute=request.POST['institute'],
            description=request.POST['description']
        )
        qualification.save()
        resume.qualifications.add(qualification)

        return redirect('add_experience', resume_id=resume_id)

    return render(request, 'add_qualifications.html', {'resume': resume})

def add_experience(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    if request.method == 'POST':
        experience = Experiance(
            companyname=request.POST['companyname'],
            position=request.POST['position'],
            startdate=request.POST['startdate'],
            enddate=request.POST['enddate'],
            projects=request.POST['projects'],
            project_discription=request.POST['project_discription'],
            responsibilities=request.POST['responsibilities'],
            jobdescription=request.POST['jobdescription']
        )
        experience.save()
        resume.experiences.add(experience)

        return redirect('resume_preview', resume_id=resume_id)

    return render(request, 'add_experience.html', {'resume': resume})

def resume_preview(request, resume_id):
    resume = Resume.objects.get(id=resume_id)
    return render(request, 'resume_preview.html', {'resume': resume})