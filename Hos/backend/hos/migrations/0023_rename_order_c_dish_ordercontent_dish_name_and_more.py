# Generated by Django 4.2.5 on 2023-10-19 13:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0022_remove_ordercontent_order_c_dish_amount_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ordercontent',
            old_name='order_c_dish',
            new_name='dish_name',
        ),
        migrations.RenameField(
            model_name='ordercontent',
            old_name='order_c_dish_qty',
            new_name='dish_qty',
        ),
        migrations.RenameField(
            model_name='ordercontent',
            old_name='order_c_order',
            new_name='order',
        ),
    ]
