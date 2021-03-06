# Generated by Django 3.1.4 on 2021-05-31 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0004_auto_20210528_2205'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='codingprofile',
            name='interviewbit',
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='codechef_questions',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='codeforces_questions',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='gfg',
            field=models.CharField(blank=True, default='N/A', max_length=255),
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='gfg_questions',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='leetcode_questions',
            field=models.CharField(default='0', max_length=255),
        ),
        migrations.AddField(
            model_name='codingprofile',
            name='spoj_questions',
            field=models.CharField(default='0', max_length=255),
        ),
    ]
