# Generated by Django 3.1 on 2021-03-16 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0002_auto_20210316_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventinfo',
            name='begins_on',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='created',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='eventinfo',
            name='ends_on',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
