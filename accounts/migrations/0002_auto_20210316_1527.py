# Generated by Django 3.1 on 2021-03-16 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='profile_url',
            field=models.ImageField(blank=True, default=False, null=True, upload_to=''),
        ),
    ]
