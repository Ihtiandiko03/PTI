# Generated by Django 3.2.9 on 2022-04-13 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='editor',
            fields=[
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('nama', models.CharField(max_length=255, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
