# Generated by Django 4.1.2 on 2022-10-11 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='money',
            name='name',
            field=models.TextField(null=True),
        ),
    ]