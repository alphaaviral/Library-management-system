# Generated by Django 3.2 on 2021-04-20 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_book_isbn'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ISBN',
            field=models.CharField(default='000-000-000-000-0', max_length=17),
        ),
    ]
