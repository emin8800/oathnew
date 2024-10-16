# Generated by Django 5.1.1 on 2024-10-07 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0023_remove_customuser_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='telephone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='verification_code',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
