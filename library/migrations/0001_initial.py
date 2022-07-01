# Generated by Django 3.2.4 on 2022-07-01 21:38

from django.db import migrations, models
import django.db.models.deletion
import library.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pid', models.CharField(max_length=6, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Issued',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_issued', models.DateField(auto_now_add=True)),
                ('expires_on', models.DateField(default=library.models.get_expire)),
                ('isbn', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fisbn', to='library.books', to_field='isbn')),
                ('pid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fpid', to='library.person', to_field='pid')),
            ],
        ),
    ]
