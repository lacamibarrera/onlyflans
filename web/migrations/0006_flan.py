# Generated by Django 5.1.2 on 2024-10-25 21:01

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_contactform_delete_flan'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flan_uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('name', models.CharField(max_length=64)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_private', models.BooleanField(default=False)),
                ('slug', models.SlugField(max_length=64, unique=True)),
            ],
        ),
    ]