# Generated by Django 3.2.7 on 2021-09-15 15:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_buildmodel_is_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='transporttypemodel',
            name='is_base',
            field=models.BooleanField(default=False),
        ),
    ]