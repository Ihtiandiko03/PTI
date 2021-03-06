# Generated by Django 3.2.9 on 2022-05-05 03:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='topik',
            fields=[
                ('judul', models.CharField(max_length=255)),
                ('isi_topik', models.TextField()),
                ('tanggal_upload', models.DateField()),
                ('gambar', models.ImageField(upload_to='static/forum/%Y/%m/%d')),
                ('kategori', models.CharField(choices=[('UMKM', 'UMKM'), ('Berita', 'Berita'), ('Forum', 'Forum'), ('Rekomendasi', 'Rekomendasi'), ('Aplikasi', 'Aplikasi'), ('Serba Serbi Ramadhan', 'Serba Serbi Ramadhan'), ('Modal UMKM', 'Modal UMKM')], max_length=100)),
                ('slug', models.SlugField(blank=True, editable=False, primary_key=True, serialize=False)),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='komentar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal_upload', models.DateField()),
                ('isi_komentar', models.TextField()),
                ('id_topik', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forum.topik')),
                ('username_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
