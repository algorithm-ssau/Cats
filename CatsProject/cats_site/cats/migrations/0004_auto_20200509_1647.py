# Generated by Django 3.0.6 on 2020-05-09 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0003_auto_20200509_1642'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='life_span',
            field=models.CharField(max_length=100, verbose_name='Продолжительность жизни'),
        ),
    ]