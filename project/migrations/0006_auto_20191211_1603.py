# Generated by Django 2.2.7 on 2019-12-11 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0005_auto_20191211_1549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_model',
            name='dat',
            field=models.DateTimeField(),
        ),
    ]
