# Generated by Django 4.1.6 on 2023-03-07 21:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('card_interactions', '0007_rename_like_follower_rename_document_resource'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='follower',
            name='date_created',
        ),
        migrations.RemoveField(
            model_name='follower',
            name='date_modified',
        ),
    ]
