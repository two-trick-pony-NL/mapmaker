# Generated by Django 4.1.6 on 2023-04-05 19:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0019_rename_legend_color_legenda_icon_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='workshop',
            name='legend_1',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='legend_2',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='legend_3',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='legend_4',
        ),
        migrations.RemoveField(
            model_name='workshop',
            name='legend_5',
        ),
        migrations.DeleteModel(
            name='Legenda',
        ),
    ]
