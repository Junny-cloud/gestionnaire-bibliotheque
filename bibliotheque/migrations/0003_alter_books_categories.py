# Generated by Django 5.0.4 on 2024-05-03 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibliotheque', '0002_books_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='categories',
            field=models.ManyToManyField(to='bibliotheque.categories', verbose_name='All Categorie'),
        ),
    ]
