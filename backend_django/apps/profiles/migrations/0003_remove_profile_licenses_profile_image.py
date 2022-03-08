# Generated by Django 4.0.3 on 2022-03-08 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_alter_profile_created_at_alter_profile_updated_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='licenses',
        ),
        migrations.AddField(
            model_name='profile',
            name='Image',
            field=models.ImageField(default='/profile_default.png', upload_to='', verbose_name='Profile Picture'),
        ),
    ]
