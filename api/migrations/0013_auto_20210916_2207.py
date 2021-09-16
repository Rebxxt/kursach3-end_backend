# Generated by Django 3.2.7 on 2021-09-16 19:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_itemmodel_counter'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ordermodel',
            options={'ordering': ['-id']},
        ),
        migrations.RemoveField(
            model_name='itemmodel',
            name='order',
        ),
        migrations.CreateModel(
            name='OrderItemModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('take_counter', models.IntegerField(default=0)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.itemmodel')),
                ('order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.ordermodel')),
            ],
        ),
        migrations.AddField(
            model_name='itemmodel',
            name='order',
            field=models.ManyToManyField(related_name='items', through='api.OrderItemModel', to='api.OrderModel'),
        ),
    ]
