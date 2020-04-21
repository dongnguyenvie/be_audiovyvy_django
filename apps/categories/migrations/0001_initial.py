# Generated by Django 3.0.5 on 2020-04-21 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='', max_length=50)),
                ('description', models.TextField(default='')),
                ('status', models.CharField(default='publish', max_length=30)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('meta', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='metas.Meta')),
            ],
        ),
    ]
