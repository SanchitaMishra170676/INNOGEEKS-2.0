# Generated by Django 3.1.4 on 2021-05-16 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_otherlink_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='subtopic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.subtopic'),
        ),
        migrations.AlterField(
            model_name='topic',
            name='domain',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.course'),
        ),
    ]