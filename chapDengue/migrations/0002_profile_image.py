# Generated by Django 4.0.4 on 2022-05-15 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chapDengue', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
