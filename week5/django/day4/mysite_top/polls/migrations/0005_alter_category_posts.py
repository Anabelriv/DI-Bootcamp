# Generated by Django 4.2.4 on 2023-08-13 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='posts',
            field=models.ManyToManyField(related_name='categories', to='polls.post'),
        ),
    ]
