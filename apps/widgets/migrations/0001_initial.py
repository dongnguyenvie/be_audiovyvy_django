# Generated by Django 3.0.5 on 2020-05-07 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('metas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Widget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(default='none', max_length=30)),
                ('title', models.CharField(default='', max_length=30)),
                ('isDelete', models.BooleanField(default=False)),
                ('image', models.URLField(blank=True)),
                ('url', models.URLField(blank=True)),
                ('size', models.CharField(max_length=30)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('meta', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='metas.Meta')),
            ],
        ),
    ]
