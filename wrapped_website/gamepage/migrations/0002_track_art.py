# Generated by Django 4.2.7 on 2023-11-18 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='art',
            field=models.URLField(default='#', max_length=250),
            preserve_default=False,
        ),
    ]
