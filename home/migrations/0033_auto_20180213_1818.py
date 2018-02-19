# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-13 18:18
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0032_finalapplication_applying_to_gsoc'),
    ]

    operations = [
        migrations.CreateModel(
            name='NonCollegeSchoolTimeCommitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField(help_text='Date your coding school or online course starts. Use YYYY-MM-DD format.')),
                ('end_date', models.DateField(help_text='Date your coding school or online course ends. Use YYYY-MM-DD format.')),
                ('hours_per_week', models.IntegerField(help_text='Maximum hours per week spent on coursework, homework, and studying for this course.', validators=[django.core.validators.MinValueValidator(1)])),
                ('description', models.TextField(blank=True, help_text='Please describe the course (name, short description of course work, and link to the coding school or online coursework website).', max_length=3000)),
            ],
        ),
        migrations.AddField(
            model_name='applicantapproval',
            name='enrolled_as_noncollege_student',
            field=models.NullBooleanField(help_text='Will you be enrolled in a coding school or self-paced online classes during the Outreachy internship period?'),
        ),
        migrations.AlterField(
            model_name='applicantapproval',
            name='volunteer_time_commitments',
            field=models.NullBooleanField(help_text='Will you have any volunteer positions (such as volunteering with a non-profit or community center, participating in a community band, or volunteering to organize an event) that require more than 10 hours a week during the Outreachy internship period? Do not count your Outreachy internship time as a volunteer position.'),
        ),
        migrations.AlterField(
            model_name='finalapplication',
            name='applying_to_gsoc',
            field=models.TextField(blank=True, help_text='If you are a student at an accredited university or college, we highly encourage you to also apply to <a href="https://summerofcode.withgoogle.com/">Google Summer of Code</a> during the May to August internship round. Many Outreachy communities participate in both programs, and applying to Google Summer of Code increases your chances of being accepted as an intern. Please note that <a href="https://developers.google.com/open-source/gsoc/help/student-stipends">Google Summer of Code has stipend amounts that vary per country</a>.<br><br>Please keep the list of communities and projects you are applying to under Google Summer of Code up-to-date, since we often try to coordinate with Google Summer of Code mentors during the intern selection period.<br><br>If this application is for the December to March internship period, or you are not applying to Google Summer of Code, please leave this question blank.', max_length=8000, verbose_name='(Optional) Please describe which Google Summer of Code communities and projects you are applying for, and provide mentor contact information'),
        ),
        migrations.AddField(
            model_name='noncollegeschooltimecommitment',
            name='applicant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.ApplicantApproval'),
        ),
    ]