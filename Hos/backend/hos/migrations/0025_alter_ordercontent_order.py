# Generated by Django 4.2.5 on 2023-10-19 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0024_remove_payment_payment_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ordercontent',
            name='order',
            field=models.CharField(max_length=100),
        ),
    ]
