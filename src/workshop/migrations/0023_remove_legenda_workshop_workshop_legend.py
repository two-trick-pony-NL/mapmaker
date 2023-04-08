# Generated by Django 4.1.6 on 2023-04-05 19:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0022_remove_legenda_legend_color_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='legenda',
            name='workshop',
        ),
        migrations.AddField(
            model_name='workshop',
            name='legend',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='workshoplegend', to='workshop.legenda'),
        ),
    ]