# Generated by Django 3.0.8 on 2020-07-25 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gym', '0007_auto_20200704_0850'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercise',
            name='category',
            field=models.CharField(choices=[('male', 'male'), ('female', 'female')], default='male', max_length=20),
        ),
    ]
