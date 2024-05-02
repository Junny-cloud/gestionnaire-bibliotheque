# Generated by Django 3.2.5 on 2024-05-02 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, unique=True, verbose_name='Nom categorie')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('date_registry', models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('status', models.BooleanField(default=True, verbose_name='Etat')),
            ],
            options={
                'verbose_name': 'Categorie',
                'verbose_name_plural': 'Categories',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Nom livre')),
                ('slug', models.SlugField(null=True, unique=True)),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('date_registry', models.DateTimeField(auto_now_add=True, verbose_name="Date d'enregistrement")),
                ('date_modification', models.DateTimeField(auto_now=True, verbose_name='Date de modification')),
                ('status', models.BooleanField(default=True, verbose_name='Etat')),
                ('categories', models.ManyToManyField(blank=True, to='bibliotheque.Categories', verbose_name='All Categorie')),
            ],
            options={
                'verbose_name': 'Livre',
                'verbose_name_plural': 'Livres',
                'ordering': ['-id'],
            },
        ),
    ]