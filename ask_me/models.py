from django.db import models

# Create your models here.

class Questions(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50, verbose_name= "Ad Soyad", default="Ecem Bekar")
    mail = models.EmailField(verbose_name="E-mail")
    subject = models.CharField(max_length=150, verbose_name="Konu",default="")
    question = models.TextField(verbose_name="Soru")
    answer = models.TextField(blank=True, null=True,verbose_name="Cevap")
    is_public = models.BooleanField(choices=[(True, 'Public'), (False, 'Private')], verbose_name="Yayınlansın Mı?")

    def __str__(self):
        return f'{self.pk}: {"Public" if self.is_public else "Private"}' + " : " + self.question