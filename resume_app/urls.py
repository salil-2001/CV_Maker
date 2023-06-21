from django.urls import path
from .views import choose_template, create_resume, add_qualifications, add_experience, resume_preview

urlpatterns = [
    path('choose-template/', choose_template, name='choose_template'),
    path('create-resume/<int:template_id>/', create_resume, name='create_resume'),
    path('add-qualifications/<int:resume_id>/', add_qualifications, name='add_qualifications'),
    path('add-experience/<int:resume_id>/', add_experience, name='add_experience'),
    path('resume-preview/<int:resume_id>/', resume_preview, name='resume_preview'),
]