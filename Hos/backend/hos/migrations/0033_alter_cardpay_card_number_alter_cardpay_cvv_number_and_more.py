# Generated by Django 4.2.5 on 2023-11-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0032_cardpay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardpay',
            name='card_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cardpay',
            name='cvv_number',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cardpay',
            name='expire_date',
            field=models.CharField(max_length=20),
        ),
    ]