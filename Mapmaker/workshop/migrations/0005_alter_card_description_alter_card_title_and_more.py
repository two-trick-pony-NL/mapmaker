# Generated by Django 4.1.6 on 2023-02-25 19:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0004_alter_card_author_alter_card_followers_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='card',
            name='title',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_name',
            field=models.CharField(max_length=30, unique=True),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='workshop_owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='workshop_owners', to=settings.AUTH_USER_MODEL),
        ),
    ]