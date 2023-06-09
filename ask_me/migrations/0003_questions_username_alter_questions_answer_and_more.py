# Generated by Django 4.1.7 on 2023-04-14 04:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ask_me', '0002_alter_questions_answer'),
    ]

    operations = [
        migrations.AddField(
            model_name='questions',
            name='username',
            field=models.CharField(default='Ecem Bekar', max_length=50, verbose_name='Ad Soyad'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='answer',
            field=models.TextField(blank=True, null=True, verbose_name='Cevap'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='is_public',
            field=models.BooleanField(choices=[(True, 'Public'), (False, 'Private')], verbose_name='Yayınlansın Mı?'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='mail',
            field=models.EmailField(max_length=254, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='questions',
            name='question',
            field=models.TextField(verbose_name='Soru'),
        ),
    ]
