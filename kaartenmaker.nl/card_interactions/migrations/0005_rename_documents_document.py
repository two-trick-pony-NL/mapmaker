# Generated by Django 4.1.6 on 2023-02-25 10:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0004_alter_card_author_alter_card_followers_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card_interactions', '0004_documents'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='documents',
            new_name='Document',
        ),
    ]
