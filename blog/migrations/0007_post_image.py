# Generated by Django 4.2.6 on 2023-10-25 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='blog/defualt.jpg', upload_to='blog/'),
        ),
    ]