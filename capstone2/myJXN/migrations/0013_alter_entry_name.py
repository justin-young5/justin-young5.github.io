# Generated by Django 4.1.2 on 2022-10-29 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myJXN', '0012_entry_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
