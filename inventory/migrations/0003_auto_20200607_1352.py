# Generated by Django 3.0.7 on 2020-06-07 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200606_1612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='count',
            new_name='amount',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='serial_number',
            new_name='barcode',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='price_p_p',
            new_name='price_piece',
        ),
    ]