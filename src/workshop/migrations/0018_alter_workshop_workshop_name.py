# Generated by Django 4.1.6 on 2023-03-18 20:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0017_legenda_legend_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='workshop_name',
            field=models.CharField(max_length=30),
        ),
    ]