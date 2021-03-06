# Generated by Django 3.2.9 on 2022-04-12 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data_umkm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama_pemilik', models.CharField(max_length=200)),
                ('nama_umkm', models.CharField(max_length=200)),
                ('alamat', models.TextField()),
                ('kecamatan', models.CharField(max_length=200)),
                ('foto_kedai', models.ImageField(upload_to='')),
                ('logo', models.ImageField(upload_to='')),
                ('daftar_produk', models.TextField()),
                ('foto_produk', models.ImageField(upload_to='')),
            ],
        ),
    ]
