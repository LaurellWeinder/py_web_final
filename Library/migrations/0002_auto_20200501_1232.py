# Generated by Django 3.0.3 on 2020-05-01 12:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Library', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['-author_id']},
        ),
        migrations.AlterModelOptions(
            name='book',
            options={'ordering': ['-book_id']},
        ),
    ]