# Generated by Django 3.0.5 on 2020-07-20 07:37

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.TextField(default='', max_length=30)),
                ('content', models.TextField(default='')),
                ('isDeleted', models.BooleanField(default=False)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='metas.Meta')),
            ],
        ),
    ]
