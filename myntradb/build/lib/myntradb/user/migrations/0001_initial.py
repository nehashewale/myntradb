# Generated by Django 2.1 on 2021-07-20 16:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('landmark', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=20)),
                ('taluka', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('pincode', models.IntegerField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('phone_number', models.IntegerField(default=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=2)),
                ('date_of_birth', models.DateField(default=True)),
                ('primary_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='primary_address', to='user.Address')),
                ('shipping_address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shipping_address', to='user.Address')),
            ],
        ),
    ]
