# Generated by Django 3.0.5 on 2020-04-18 07:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meta',
            name='type',
            field=models.CharField(db_index=True, max_length=10, null=True),
        ),
    ]
