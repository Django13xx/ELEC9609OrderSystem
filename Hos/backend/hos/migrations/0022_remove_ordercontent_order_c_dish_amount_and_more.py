# Generated by Django 4.2.5 on 2023-10-19 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0021_remove_menu_dish_pic'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordercontent',
            name='order_c_dish_amount',
        ),
        migrations.RemoveField(
            model_name='ordercontent',
            name='order_c_note',
        ),
        migrations.AlterField(
            model_name='ordercontent',
            name='order_c_dish',
            field=models.CharField(max_length=100),
        ),
    ]
