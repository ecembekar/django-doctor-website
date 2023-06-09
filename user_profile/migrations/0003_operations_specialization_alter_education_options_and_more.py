# Generated by Django 4.1.7 on 2023-04-14 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_education_ongoing_experience_ongoing_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Operations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Başlık')),
                ('amount', models.IntegerField(verbose_name='Miktarı')),
            ],
        ),
        migrations.CreateModel(
            name='Specialization',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Başlık')),
                ('info', models.CharField(max_length=200, verbose_name='Kısa Bilgi')),
            ],
        ),
        migrations.AlterModelOptions(
            name='education',
            options={'ordering': ['-end_year']},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='adress',
        ),
        migrations.AddField(
            model_name='profile',
            name='about',
            field=models.TextField(default=' ', verbose_name='Hakkımda'),
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.TextField(default=' ', verbose_name='Adres'),
        ),
        migrations.AddField(
            model_name='profile',
            name='birth_year',
            field=models.DateField(default='1964-12-21', verbose_name='Doğum Tarihi'),
        ),
        migrations.AddField(
            model_name='profile',
            name='city',
            field=models.CharField(default='Konya', max_length=30, verbose_name='Şehir'),
        ),
        migrations.AddField(
            model_name='profile',
            name='title',
            field=models.CharField(default='Prof. Dr.', max_length=20, verbose_name='Ünvan'),
        ),
        migrations.AlterField(
            model_name='education',
            name='department_name',
            field=models.CharField(max_length=100, verbose_name='Bölüm Adı'),
        ),
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bitiş Yılı'),
        ),
        migrations.AlterField(
            model_name='education',
            name='ongoing',
            field=models.BooleanField(default=False, verbose_name='Devam Ediyor'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school_name',
            field=models.CharField(max_length=100, verbose_name='Okul Adı'),
        ),
        migrations.AlterField(
            model_name='education',
            name='school_type',
            field=models.CharField(choices=[('Lise', 'Lise'), ('Önlisans', 'Önlisans'), ('Lisans', 'Lisans'), ('Yüksek_Lisans', 'Yüksek_Lisans')], default='Lise', max_length=14, verbose_name='Eğitim Seviyesi'),
        ),
        migrations.AlterField(
            model_name='education',
            name='start_year',
            field=models.IntegerField(verbose_name='Başlangıç Yılı'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='company_name',
            field=models.CharField(max_length=100, verbose_name='Firma Adı'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_year',
            field=models.IntegerField(blank=True, null=True, verbose_name='Bitiş Yılı'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='ongoing',
            field=models.BooleanField(default=False, verbose_name='Devam Ediyor'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='position',
            field=models.CharField(max_length=100, verbose_name='Pozisyon'),
        ),
        migrations.AlterField(
            model_name='experience',
            name='start_year',
            field=models.IntegerField(verbose_name='Başlangıç Yılı'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(max_length=20, verbose_name='Ad'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone_number',
            field=models.CharField(max_length=11, verbose_name='Telefon'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='surname',
            field=models.CharField(max_length=20, verbose_name='Soyad'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='content',
            field=models.TextField(verbose_name='İçerik'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Yayın Adı'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='publication_type',
            field=models.CharField(choices=[('Kitap', 'Kitap'), ('Makale', 'Makale'), ('Bildiri', 'Bildiri'), ('Proje', 'Proje')], default='Kitap', max_length=10, verbose_name='Yayın Türü'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='subject',
            field=models.CharField(max_length=350, verbose_name='Yayın Konusu'),
        ),
        migrations.AlterField(
            model_name='publications',
            name='year',
            field=models.IntegerField(verbose_name='Yayın Yılı'),
        ),
    ]
