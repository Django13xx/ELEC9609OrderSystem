# Generated by Django 4.2.5 on 2023-10-24 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0029_alter_payment_payment_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='staff_status',
            field=models.BooleanField(default=False),
        ),
    ]
