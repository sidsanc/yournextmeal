# Generated by Django 4.1.2 on 2022-11-21 05:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DbOperationsApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='requeststatus',
            old_name='RequestStatus',
            new_name='RequestCurrentStatus',
        ),
    ]
