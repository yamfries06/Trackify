# Generated by Django 5.1 on 2024-09-10 00:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-date']},
        ),
    ]
