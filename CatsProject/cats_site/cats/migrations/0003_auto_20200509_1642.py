# Generated by Django 3.0.6 on 2020-05-09 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0002_auto_20200509_1604'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='about',
            field=models.CharField(max_length=1000, verbose_name='О породе'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='height',
            field=models.CharField(max_length=100, verbose_name='Рост'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='lifestyle',
            field=models.CharField(max_length=1000, verbose_name='Образ жизни'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='qualities',
            field=models.CharField(max_length=500, verbose_name='Качесва'),
        ),
        migrations.AlterField(
            model_name='cat',
            name='weight',
            field=models.CharField(max_length=100, verbose_name='Вес'),
        ),
    ]