# Generated by Django 4.1.6 on 2023-02-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school_name', models.CharField(max_length=225)),
                ('degree', models.CharField(max_length=50)),
                ('area_of_study', models.CharField(max_length=75)),
                ('date_attended', models.CharField(max_length=50)),
                ('school_location', models.CharField(max_length=100)),
                ('accolade', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Hobby',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('dates_practiced', models.CharField(max_length=100)),
                ('description', models.CharField(blank=True, max_length=250)),
                ('url', models.URLField(blank=True, max_length=225)),
            ],
        ),
        migrations.CreateModel(
            name='OtherWorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=225)),
                ('company_name', models.CharField(max_length=300)),
                ('company_location', models.CharField(max_length=250)),
                ('dates_employed', models.CharField(max_length=250)),
                ('job_description', models.CharField(max_length=350)),
                ('additional_job_description', models.CharField(blank=True, max_length=400)),
                ('specialization', models.CharField(blank=True, max_length=250)),
                ('special_info', models.CharField(blank=True, max_length=250)),
                ('special_info_2', models.CharField(blank=True, max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('level', models.CharField(choices=[('AL', 'Advanced'), ('FL', 'Familiar'), ('OL', 'Other')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=125)),
                ('proficiency', models.CharField(choices=[('HP', 'High'), ('MP', 'Medium'), ('LP', 'Low')], max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='WorkExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position_title', models.CharField(max_length=225)),
                ('company_name', models.CharField(max_length=300)),
                ('company_location', models.CharField(max_length=250)),
                ('dates_employed', models.CharField(max_length=250)),
                ('job_description', models.CharField(max_length=350)),
                ('additional_job_description', models.CharField(blank=True, max_length=400)),
            ],
        ),
    ]
