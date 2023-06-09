# Generated by Django 4.1.5 on 2023-02-22 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['author__last_name', 'title'], 'verbose_name': 'Bookington', 'verbose_name_plural': 'Bookington McBookFace'},
        ),
        migrations.AddField(
            model_name='author',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AddIndex(
            model_name='book',
            index=models.Index(fields=['title', 'author'], name='catalog_boo_title_5b6232_idx'),
        ),
    ]
