# Generated by Django 4.1.6 on 2023-02-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0007_remove_card_xcoordinate_remove_card_ycoordinate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='parentnode',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='workshop.card'),
        ),
    ]
