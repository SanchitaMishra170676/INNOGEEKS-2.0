# Generated by Django 3.1.4 on 2021-05-08 08:02

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('teamName', models.CharField(max_length=100)),
                ('rank', models.CharField(max_length=100)),
                ('prize', models.CharField(blank=True, max_length=100)),
                ('poster', models.ImageField(default='', upload_to='media/Home/Achievements/')),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='CarouselImg',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(default='', upload_to='media/Home/CarouselImgs')),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=800)),
                ('subject', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=255)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('answered', models.BooleanField(default=False)),
                ('email_subject', models.CharField(blank=True, max_length=200, null=True)),
                ('email_body', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Core_Team_Member',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('branch', models.CharField(blank=True, max_length=255)),
                ('year', models.CharField(blank=True, max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('linkedIn', models.CharField(blank=True, max_length=255)),
                ('gitHub', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('coreImage', models.ImageField(default='', upload_to='media/Home/core_team_members/')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='DeveloperTeam',
            fields=[
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('linkedIn', models.CharField(blank=True, max_length=255)),
                ('intro', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(default='', upload_to='media/Home/Developers/')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('domainImage', models.ImageField(default='', upload_to='media/Home/Domain/')),
            ],
        ),
        migrations.CreateModel(
            name='Founder',
            fields=[
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('linkedIn', models.CharField(blank=True, max_length=255)),
                ('gitHub', models.CharField(blank=True, max_length=255)),
                ('instagram', models.CharField(blank=True, max_length=255)),
                ('facebook', models.CharField(blank=True, max_length=255)),
                ('coreImage', models.ImageField(default='', upload_to='media/Home/Founders/')),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('image', models.ImageField(default='', upload_to='media/Home/Gallery')),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
                ('formLink', models.CharField(max_length=500)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='Recruitment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=10)),
                ('branch', models.CharField(max_length=10)),
                ('hostel', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone', models.CharField(max_length=10, unique=True)),
                ('domain', models.CharField(max_length=100)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('selection1', models.BooleanField(default=False)),
                ('selection2', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('message', models.TextField(max_length=300)),
                ('Image', models.ImageField(default='', upload_to='media/Home/Testimonials/')),
                ('position', models.CharField(max_length=150)),
                ('active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('desc', models.CharField(max_length=255)),
                ('link', models.CharField(blank=True, max_length=255)),
                ('active', models.BooleanField(default=False)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.CreateModel(
            name='VolunteerTeam',
            fields=[
                ('name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('linkedIn', models.CharField(blank=True, max_length=255)),
                ('intro', models.CharField(blank=True, max_length=255)),
                ('image', models.ImageField(default='', upload_to='media/Home/Volunteers/')),
                ('active', models.BooleanField(default=False)),
            ],
        ),
    ]
