# Generated by Django 3.0.5 on 2020-04-21 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(blank=True, default=''),
        ),
        migrations.AlterField(
            model_name='post',
            name='excerpt',
            field=models.TextField(blank=True, default=''),
        ),
    ]