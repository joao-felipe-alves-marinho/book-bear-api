# Generated by Django 5.2 on 2025-04-10 23:16

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BookBearApi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('birth_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publisher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='followed_authors',
            field=models.ManyToManyField(blank=True, related_name='followers', to='BookBearApi.author'),
        ),
        migrations.AddField(
            model_name='user',
            name='favorite_genres',
            field=models.ManyToManyField(blank=True, related_name='users', to='BookBearApi.genre'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('publication_date', models.DateField()),
                ('synopsis', models.TextField(blank=True)),
                ('score', models.FloatField()),
                ('age_rating', models.CharField(choices=[('AA', 'All Ages'), ('T', 'Teen'), ('M', 'Mature'), ('A', 'Adult')], default='AA', max_length=2)),
                ('authors', models.ManyToManyField(to='BookBearApi.author')),
                ('genres', models.ManyToManyField(to='BookBearApi.genre')),
                ('publisher', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='BookBearApi.publisher')),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='followed_publishers',
            field=models.ManyToManyField(blank=True, related_name='followers', to='BookBearApi.publisher'),
        ),
        migrations.CreateModel(
            name='UserBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('situation', models.CharField(choices=[('R', 'Reading'), ('S', 'Stopped'), ('C', 'Completed'), ('P', 'Pending')], default='R', max_length=2)),
                ('rating', models.FloatField(blank=True, null=True)),
                ('review', models.TextField(blank=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookBearApi.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'book')},
            },
        ),
        migrations.AddField(
            model_name='user',
            name='reviewed_books',
            field=models.ManyToManyField(blank=True, related_name='reviews', through='BookBearApi.UserBook', to='BookBearApi.book'),
        ),
    ]
