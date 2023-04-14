# Generated by Django 3.2.7 on 2021-09-29 08:28

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('picapp', '0003_auto_20210929_0827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, null=True, populate_from='title', unique=True),
        ),
        migrations.AlterField(
            model_name='photo',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='picapp.album'),
        ),
    ]