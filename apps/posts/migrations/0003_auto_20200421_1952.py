# Generated by Django 3.0.5 on 2020-04-21 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20200421_1856'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type',
            field=models.CharField(choices=[(1, 'post'), (2, 'video'), (3, 'audio'), (4, 'image'), (5, 'other')], default=1, max_length=2),
        ),
    ]
