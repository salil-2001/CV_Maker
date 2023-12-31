# Generated by Django 4.2.2 on 2023-06-21 10:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Experiance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companyname', models.CharField(max_length=200)),
                ('position', models.CharField(max_length=300)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('projects', models.CharField(max_length=50)),
                ('project_discription', models.TextField()),
                ('responsibilities', models.TextField()),
                ('jobdescription', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Qualifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=100)),
                ('college', models.CharField(max_length=100)),
                ('year', models.DateField()),
                ('course', models.CharField(max_length=100)),
                ('institute', models.CharField(max_length=100)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='ResumeTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('Position', models.CharField(max_length=50)),
                ('contact', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('about', models.TextField()),
                ('template', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='resume_app.resumetemplate')),
            ],
        ),
    ]
