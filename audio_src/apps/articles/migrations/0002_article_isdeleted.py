# Generated by Django 3.0.5 on 2020-07-15 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='isDeleted',
            field=models.BooleanField(default=False),
        ),
    ]
