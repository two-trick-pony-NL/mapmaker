# Generated by Django 4.1.6 on 2023-02-25 10:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workshop', '0003_card_delete_abmbition_workshop_is_active_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='card',
            name='followers',
            field=models.ManyToManyField(related_name='card_followers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='workshop',
            name='participants',
            field=models.ManyToManyField(related_name='workshop_participants', to=settings.AUTH_USER_MODEL),
        ),
    ]