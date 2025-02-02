# Generated by Django 5.0.6 on 2024-06-25 05:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lessons',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(choices=[('ПН', 'Понедельник'), ('ВТ', 'Вторник'), ('СРЕ', 'Среда'), ('ЧТ', 'Четверг'), ('ПЯТ', 'Пятница'), ('СУБ', 'Суббота')], max_length=355)),
                ('start_time', models.TimeField()),
                ('time_duration', models.PositiveIntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edu_app.courses')),
            ],
        ),
    ]
