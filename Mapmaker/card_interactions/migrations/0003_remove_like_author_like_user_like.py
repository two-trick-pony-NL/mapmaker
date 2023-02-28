# Generated by Django 4.1.6 on 2023-02-25 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card_interactions', '0002_rename_comments_comment_rename_likes_like'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='like',
            name='author',
        ),
        migrations.AddField(
            model_name='like',
            name='user_like',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_like', to=settings.AUTH_USER_MODEL),
        ),
    ]