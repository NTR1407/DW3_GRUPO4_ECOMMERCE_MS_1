# Generated by Django 3.2.6 on 2021-08-20 03:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceUsersApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ecommerceuser',
            name='address',
            field=models.CharField(default='46 St.', max_length=500),
        ),
        migrations.AddField(
            model_name='ecommerceuser',
            name='telephone',
            field=models.IntegerField(default=12345, max_length=500),
        ),
    ]
