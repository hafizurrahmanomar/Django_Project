# Generated by Django 4.2.6 on 2023-10-20 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myblogpost',
            name='created_at',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='myblogpost',
            name='updated_at',
            field=models.DateTimeField(),
        ),
    ]
