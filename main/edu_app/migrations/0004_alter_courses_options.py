# Generated by Django 5.0.6 on 2024-06-25 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0003_alter_student_options_alter_student_managers_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='courses',
            options={'ordering': ['-duration'], 'verbose_name': 'Course', 'verbose_name_plural': 'Courses'},
        ),
    ]
