# Generated by Django 2.2.7 on 2019-12-11 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0006_auto_20191211_1603'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback_model',
            name='dat',
            field=models.DateTimeField(max_length=50),
        ),
    ]