# Generated by Django 4.0.6 on 2022-08-01 00:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('BlogApp', '0002_remove_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=django.utils.timezone.now, editable=False),
        ),
    ]