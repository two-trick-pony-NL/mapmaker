# Generated by Django 4.1.6 on 2023-04-16 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0038_legenda'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
