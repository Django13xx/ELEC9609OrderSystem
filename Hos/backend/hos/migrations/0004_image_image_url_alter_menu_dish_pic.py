# Generated by Django 4.2.5 on 2023-10-07 06:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0003_image_alter_menu_dish_pic'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='image_url',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hos.menu'),
        ),
        migrations.AlterField(
            model_name='menu',
            name='dish_pic',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
