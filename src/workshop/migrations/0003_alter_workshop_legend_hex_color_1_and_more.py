# Generated by Django 4.1.6 on 2023-04-28 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_workshop_legend_hex_color_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workshop',
            name='legend_hex_color_1',
            field=models.CharField(default='00000', max_length=6),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='legend_hex_color_5',
            field=models.CharField(default='78E7BF', max_length=6),
        ),
    ]
