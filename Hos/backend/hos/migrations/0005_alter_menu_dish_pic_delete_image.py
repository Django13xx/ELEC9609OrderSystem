# Generated by Django 4.2.5 on 2023-10-07 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hos', '0004_image_image_url_alter_menu_dish_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menu',
            name='dish_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
