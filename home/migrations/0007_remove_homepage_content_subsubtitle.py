# Generated by Django 3.0.3 on 2022-01-04 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_homepage_content_subsubtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='homepage',
            name='content_subSubtitle',
        ),
    ]
