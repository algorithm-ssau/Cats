# Generated by Django 3.0.6 on 2020-05-22 19:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0008_auto_20200522_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeofwool',
            name='text_style',
            field=models.CharField(default='button2 ', max_length=100, verbose_name='Стиль отбражения текста'),
        ),
    ]
