# Generated by Django 4.2.6 on 2023-10-27 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0030_staff_staff_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_qty',
            field=models.IntegerField(default=0),
        ),
    ]
