# Generated by Django 3.2.3 on 2022-05-09 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disabled_address_lists', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disabledadressesmodel',
            name='blackout_datetime',
            field=models.CharField(default='09.05.2022-22.01', max_length=20, verbose_name='дата и время отключения'),
        ),
    ]
