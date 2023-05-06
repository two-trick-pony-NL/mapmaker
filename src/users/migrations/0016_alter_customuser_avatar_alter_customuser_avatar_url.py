# Generated by Django 4.1.6 on 2023-05-06 12:49

from django.db import migrations, models
import thumbnails.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_alter_customuser_avatar_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=thumbnails.fields.ImageField(blank=True, null=True, upload_to='media/avatars/'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar_url',
            field=models.CharField(blank=True, default='https://api.dicebear.com/5.x/pixel-art/svg?seed=114', max_length=500),
        ),
    ]
