# Generated by Django 3.1.1 on 2020-09-09 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0003_todoitem_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoitem',
            name='category',
            field=models.CharField(default=1, max_length=100),
        ),
    ]