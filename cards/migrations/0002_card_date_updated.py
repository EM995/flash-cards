# Generated by Django 4.0.6 on 2022-07-28 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='date_updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
