# Generated by Django 4.1.6 on 2023-02-25 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='preferredname',
        ),
    ]