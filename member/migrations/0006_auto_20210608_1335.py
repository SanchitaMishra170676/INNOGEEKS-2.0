# Generated by Django 3.1.4 on 2021-06-08 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0005_auto_20210601_0011'),
    ]

    operations = [
        migrations.AlterField(
            model_name='codingprofile',
            name='codechef_questions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='codingprofile',
            name='codeforces_questions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='codingprofile',
            name='gfg_questions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='codingprofile',
            name='leetcode_questions',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='codingprofile',
            name='spoj_questions',
            field=models.IntegerField(default=0),
        ),
    ]
