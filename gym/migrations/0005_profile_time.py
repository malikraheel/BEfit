# Generated by Django 3.0.6 on 2020-06-26 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0004_auto_20200624_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='time',
            field=models.IntegerField(blank='True', default=1, null=True),
        ),
    ]
