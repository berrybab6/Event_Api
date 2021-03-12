# Generated by Django 3.1 on 2021-03-12 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('username', models.CharField(default=False, max_length=100, unique=True)),
                ('email', models.CharField(max_length=120, null=True)),
                ('password', models.CharField(max_length=255, null=True)),
                ('gender', models.CharField(max_length=12, null=True)),
                ('profile_url', models.URLField()),
                ('reset_link', models.CharField(max_length=255, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
