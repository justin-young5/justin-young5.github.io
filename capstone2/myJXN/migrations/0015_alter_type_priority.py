# Generated by Django 4.1.2 on 2022-11-01 03:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myJXN', '0014_alter_entry_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='type',
            name='priority',
            field=models.CharField(choices=[('Community Event', 'Community Event'), ('Hazard', 'Hazard'), ('Information', 'Information'), ('Building', 'Building')], max_length=20),
        ),
    ]
