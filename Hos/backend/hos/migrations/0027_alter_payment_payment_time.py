# Generated by Django 4.2.5 on 2023-10-20 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0026_alter_payment_payment_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='payment_time',
            field=models.FloatField(),
        ),
    ]
