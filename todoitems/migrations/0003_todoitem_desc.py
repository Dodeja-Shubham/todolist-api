# Generated by Django 3.1.1 on 2020-09-09 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todoitems', '0002_todoitem_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='todoitem',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
