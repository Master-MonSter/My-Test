# Generated by Django 4.2.6 on 2023-10-25 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_rename_update_date_contact_updated_date'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['created_date']},
        ),
    ]
