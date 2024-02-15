# Generated by Django 4.2.4 on 2023-10-16 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0009_delete_image_alter_menu_dish_pic'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customerdetail',
            old_name='customer_id',
            new_name='customer',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='order_table_id',
            new_name='order_table',
        ),
        migrations.RenameField(
            model_name='ordercontent',
            old_name='order_c_dish_id',
            new_name='order_c_dish',
        ),
        migrations.RenameField(
            model_name='ordercontent',
            old_name='order_id',
            new_name='order_c_order',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_address',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='staff_note',
        ),
        migrations.AddField(
            model_name='order',
            name='order_numberOfPeople',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
