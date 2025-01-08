# Generated by Django 5.1.4 on 2025-01-06 13:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='description_footer',
            field=models.TextField(default=1, verbose_name='Описние нижний заголовок'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='title_footer',
            field=models.CharField(default=1, max_length=255, verbose_name='Нижний заголовок'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='phone',
            field=models.BigIntegerField(max_length=255, verbose_name='Номер телефона'),
        ),
    ]
