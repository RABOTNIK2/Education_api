# Generated by Django 5.0.6 on 2024-06-25 09:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0004_alter_courses_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lessons',
            options={'ordering': ['-time_duration'], 'verbose_name': 'Lesson', 'verbose_name_plural': 'Lessons'},
        ),
    ]
