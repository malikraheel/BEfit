# Generated by Django 3.0.6 on 2020-06-24 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0002_contact_question'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chest', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_no',
            field=models.CharField(blank=True, max_length=15, null=True, validators=[django.core.validators.RegexValidator('[0]{1}[3]{1}[0-9]{2}[-]{1}[0-9]{7}$')]),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pic',
            field=models.ImageField(null=True, upload_to='images/'),
        ),
    ]
