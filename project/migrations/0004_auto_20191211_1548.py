# Generated by Django 2.2.7 on 2019-12-11 10:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0003_auto_20191211_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback_model',
            name='dat',
            field=models.DateTimeField(default=False, max_length=50),
        ),
        migrations.AlterField(
            model_name='feedback_model',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]