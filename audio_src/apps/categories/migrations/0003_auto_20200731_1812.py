# Generated by Django 3.0.5 on 2020-07-31 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0002_auto_20200723_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
    ]
