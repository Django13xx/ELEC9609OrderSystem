# Generated by Django 4.2.5 on 2023-10-18 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0014_alter_order_order_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]