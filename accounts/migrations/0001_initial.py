# Generated by Django 4.0.1 on 2022-02-05 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=156, unique=True)),
                ('email', models.EmailField(max_length=157, unique=True)),
                ('active', models.BooleanField(default=False)),
                ('full_name', models.CharField(max_length=256)),
                ('phone', models.CharField(max_length=15, unique=True)),
                ('town', models.CharField(max_length=57)),
            ],
        ),
    ]
