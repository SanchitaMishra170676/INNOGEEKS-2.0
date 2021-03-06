# Generated by Django 3.1.5 on 2021-05-14 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='code',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='content',
            name='image',
            field=models.ImageField(blank=True, upload_to='media/Dashboard/ContentImages/'),
        ),
        migrations.AlterField(
            model_name='content',
            name='paragraph2',
            field=models.TextField(blank=True),
        ),
    ]
