# Generated by Django 4.1.5 on 2023-02-22 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist_name',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
