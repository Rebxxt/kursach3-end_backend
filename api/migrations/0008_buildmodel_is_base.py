# Generated by Django 3.2.7 on 2021-09-15 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_rolemodel_is_base'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildmodel',
            name='is_base',
            field=models.BooleanField(default=False),
        ),
    ]
