from django.db import models

# Create your models here.

class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=20,verbose_name = "Ünvan", default="Prof. Dr.")
    name = models.CharField(max_length=20,verbose_name = "Ad")
    surname = models.CharField(max_length=20,verbose_name = "Soyad")
    email = models.EmailField(verbose_name = "E-mail")
    phone_number = models.CharField(max_length=11,verbose_name = "Telefon")
    address = models.TextField(verbose_name = "Adres", default=" ")
    city = models.CharField(max_length=30,verbose_name= "Şehir", default="Konya")
    about = models.TextField(verbose_name = "Hakkımda", default=" ")
    birth_year = models.DateField(verbose_name="Doğum Tarihi", default='1964-12-21')

    def __str__(self) -> str:
        return self.name + " " + self.surname
 
class Education(models.Model):
    school_types = [
        ('Lise', 'Lise'),
        ('Önlisans' , 'Önlisans'),
        ('Lisans' , 'Lisans'),
        ('Yüksek_Lisans' , 'Yüksek Lisans'),
        ('Doktora' , 'Doktora'),
    ]
    school_type = models.CharField(max_length=14, choices=school_types, default='Lise',verbose_name = "Eğitim Seviyesi")
    start_year = models.IntegerField(verbose_name = "Başlangıç Yılı")
    end_year = models.IntegerField(blank=True, null=True,verbose_name = "Bitiş Yılı")
    ongoing = models.BooleanField(default=False,verbose_name = "Devam Ediyor")
    school_name = models.CharField(max_length=100,verbose_name = "Okul Adı")
    department_name = models.CharField(max_length=100,verbose_name = "Bölüm Adı")
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.department_name + " / "  + self.school_name + " / " + self.school_type
    
    class Meta:
        ordering = ['-end_year']



class Experience(models.Model):
    start_year = models.IntegerField(verbose_name = "Başlangıç Yılı")
    end_year = models.IntegerField(blank=True, null=True,verbose_name = "Bitiş Yılı")
    ongoing = models.BooleanField(default=False,verbose_name = "Devam Ediyor")
    company_name = models.CharField(max_length=100,verbose_name = "Firma Adı")
    position = models.CharField(max_length=100,verbose_name = "Pozisyon")
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)
    
    def __str__(self) -> str:
        return self.position + " / "  + self.company_name 
    class Meta:
        ordering = ['-start_year']
    
class Publications(models.Model):
    publication_types = [
        ('Kitap', 'Kitap'),
        ('Makale' , 'Makale'),
        ('Bildiri' , 'Bildiri'),
        ('Proje' , 'Proje'),
    ]
    publication_type = models.TextChoices('PublicationType', publication_types)
    publication_type = models.CharField(max_length=10, choices=publication_type.choices, default= 'Kitap',verbose_name = "Yayın Türü")
    year = models.IntegerField(verbose_name = "Yayın Yılı")
    name = models.CharField(max_length=200,verbose_name = "Yayın Adı")
    subject = models.CharField(max_length=350,verbose_name = "Yayın Konusu")
    content = models.TextField(verbose_name = "İçerik") 
    profile_id = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name

class Operations(models.Model):
    title = models.CharField(max_length=100, verbose_name="Başlık")
    amount = models.IntegerField(verbose_name="Miktarı")

    def __str__(self) -> str:
        return str(self.amount) +" / "+ self.title
    
class Specialization(models.Model):
    title = models.CharField(max_length=150, verbose_name="Başlık")
    info = models.CharField(max_length=200 , verbose_name= "Kısa Bilgi")

    def __str__(self) -> str:
        return self.title