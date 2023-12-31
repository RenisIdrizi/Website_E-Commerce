# Generated by Django 4.2.2 on 2023-06-17 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_alter_order_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='address_line1',
            new_name='address_line_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='address_line2',
            new_name='address_line_2',
        ),
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Cancelled', 'Cancelled'), ('Completed', 'Completed'), ('New', 'New')], default='New', max_length=10),
        ),
    ]
