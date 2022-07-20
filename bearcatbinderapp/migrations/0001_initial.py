# Generated by Django 4.0.6 on 2022-07-19 19:41

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True, null=True)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2022, 7, 20, 19, 41, 49, 242841, tzinfo=utc))),
                ('parent_list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bearcatbinderapp.list')),
            ],
            options={
                'ordering': ['due_date'],
            },
        ),
    ]
