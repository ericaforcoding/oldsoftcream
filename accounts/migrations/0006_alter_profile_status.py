# Generated by Django 3.2.13 on 2022-11-02 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_user_followings'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='status',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]