# Generated by Django 3.2.5 on 2021-07-25 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_remove_user_date_of_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='phone_number',
            field=models.CharField(max_length=20),
        ),
    ]
