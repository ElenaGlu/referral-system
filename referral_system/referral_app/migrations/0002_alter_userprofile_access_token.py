# Generated by Django 5.0.4 on 2024-05-15 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('referral_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='access_token',
            field=models.CharField(max_length=245),
        ),
    ]