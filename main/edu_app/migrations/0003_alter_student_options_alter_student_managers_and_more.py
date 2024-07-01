# Generated by Django 5.0.6 on 2024-06-25 09:10

import django.core.validators
import edu_app.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('edu_app', '0002_lessons'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={},
        ),
        migrations.AlterModelManagers(
            name='student',
            managers=[
                ('objects', edu_app.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='student',
            name='username',
        ),
        migrations.AlterField(
            model_name='student',
            name='age',
            field=models.PositiveIntegerField(default=18, validators=[django.core.validators.MaxValueValidator(120), django.core.validators.MinValueValidator(18)]),
        ),
        migrations.AlterField(
            model_name='student',
            name='first_name',
            field=models.CharField(blank=True, max_length=30, verbose_name='first name'),
        ),
    ]
