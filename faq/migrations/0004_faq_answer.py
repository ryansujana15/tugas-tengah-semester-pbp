# Generated by Django 3.2.8 on 2021-11-05 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0003_auto_20211105_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='answer',
            field=models.TextField(default=''),
        ),
    ]