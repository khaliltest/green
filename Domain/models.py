from django.db import models
from User.models import User
from django.utils import timezone

class Image(models.Model):
    image1 = models.ImageField(blank = True)
    image2 = models.ImageField(blank = True)
    image3 = models.ImageField(blank = True)

class Rent(models.Model):
    COUNTRY_CHOICES = [
        ('IR', 'Iran'),
    ]
    CITY_CHOICES = [
        ('TEH', 'Tehran'),
        ('MAS', 'Mashhad'),
        ('ESF', 'Esfehan'),
    ]
    ZONE_CHOICES = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
        ('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
        ('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),
        ('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),
    ]
    TYPE_HOUSE = [
        ('APA', 'apartment'),
        ('VIL', 'villa'),
        ('LAN', 'land'),
    ]
    USE = [
        ('RES', 'residential'),
        ('COM', 'commercial'),
    ]
    country                        = models.CharField(choices=COUNTRY_CHOICES,
                                                      max_length=50,
                                                      verbose_name='کشور',
                                                    )
    city                           = models.CharField(choices=CITY_CHOICES,
                                                      max_length=50,
                                                      verbose_name='شهر'
                                                    )
    zone                           = models.CharField(choices=ZONE_CHOICES,
                                                      max_length=50,
                                                      verbose_name='منطقه'
                                                    )
    mortgage                       = models.DecimalField(default=0, decimal_places=2, max_digits=100000000000, verbose_name='رهن')
    rent                           = models.DecimalField(decimal_places=2, max_digits=100000000000, verbose_name='اجاره')
    area                           = models.DecimalField(decimal_places=2, max_digits=1000000, verbose_name='متراژ')
    number_of_rooms                = models.DecimalField(decimal_places=2, max_digits=7, verbose_name='تعداد اتاق')
    age_of_house                   = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='سن بنا')
    parking                        = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='پارکینگ')
    warehouse                      = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='انباری')
    elevator                       = models.BooleanField(default=True, verbose_name='آسانسور')
    balcony                        = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='بالکن')
    floors                         = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='تعداد طبفه')
    noumber_of_house_in_each_floor = models.DecimalField(decimal_places=2, max_digits=100000000000, verbose_name='تعداد واحد در هر طبقه')
    description                    = models.TextField(max_length=400, verbose_name='توضیحات')
    images                         = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True,verbose_name='تصاویر')
    yard                           = models.DecimalField(decimal_places=2, max_digits=100000000000,verbose_name='حیاط')
    area_of_ground                 = models.DecimalField(decimal_places=2, max_digits=100000000000,verbose_name='مساحت زمین')
    user                           = models.ForeignKey(User, on_delete=models.CASCADE,verbose_name='کاربر')
    type_house                     = models.CharField(choices=TYPE_HOUSE, max_length=20, verbose_name='نوع ملک')
    publish                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ساختن آگهی')
    updated                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ آپدیت')
    status                         = models.BooleanField(default=False, verbose_name='وضعیت تایید')
    code_domain                    = models.IntegerField(verbose_name='کد ملک')




class Buy(models.Model):
    COUNTRY_CHOICES = [
        ('IR', 'Iran'),
    ]
    CITY_CHOICES = [
        ('TEH', 'Tehran'),
        ('MAS', 'Mashhad'),
        ('ESF', 'Esfehan'),
    ]
    ZONE_CHOICES = [
        ('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5'),
        ('6', '6'),('7', '7'),('8', '8'),('9', '9'),('10', '10'),
        ('11', '11'),('12', '12'),('13', '13'),('14', '14'),('15', '15'),
        ('16', '16'),('17', '17'),('18', '18'),('19', '19'),('20', '20'),
    ]
    TYPE_HOUSE = [
        ('APA', 'apartment'),
        ('VIL', 'villa'),
        ('LAN', 'land'),
    ]
    USE = [
        ('RES', 'residential'),
        ('COM', 'commercial'),
    ]
    country                        = models.CharField(choices=COUNTRY_CHOICES,
                                                      max_length=50,
                                                      verbose_name='کشور'
                                                    )
    city                           = models.CharField(choices=CITY_CHOICES,
                                                      max_length=50,
                                                      verbose_name='شهر'
                                                    )
    zone                           = models.CharField(choices=ZONE_CHOICES,
                                                      max_length=50,
                                                      verbose_name='منطقه'
                                                    )
    ghadr_o_sahm                   = models.DecimalField(decimal_places=2, max_digits=1000, verbose_name='قدر السهم')
    price                          = models.DecimalField(decimal_places=2, max_digits=100000000000, verbose_name='قیمت')
    area                           = models.DecimalField(decimal_places=2, max_digits=100000, verbose_name='متراژ')
    number_of_rooms                = models.DecimalField(max_digits=7,decimal_places=2, verbose_name='تعداد اتاق')
    age_of_house                   = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='سن بنا')
    parking                        = models.DecimalField(decimal_places=2, max_digits=10000, verbose_name='پارکینگ')
    warehouse                      = models.DecimalField(decimal_places=2, max_digits=10000, verbose_name='انباری')
    elevator                       = models.BooleanField(default=True, verbose_name='آسانسور')
    balcony                        = models.DecimalField(decimal_places=2, max_digits=100000000, verbose_name='بالکن')
    floors                         = models.DecimalField(decimal_places=2, max_digits=10000000, verbose_name='تعداد طبقه')
    noumber_of_house_in_each_floor = models.DecimalField(decimal_places=2, max_digits=100, verbose_name='تعداد واحد هر طبقه')
    description                    = models.TextField(max_length=500, verbose_name='توضیحات')
    images                         = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True, verbose_name='تصاویر')
    yard                           = models.DecimalField(decimal_places=2, max_digits=100000000000, verbose_name='حیاط')
    area_of_ground                 = models.DecimalField(decimal_places=2, max_digits=100000000000, verbose_name='مساحت زمین')
    user                           = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='کاربر')
    type_house                     = models.CharField(choices=TYPE_HOUSE, max_length=20, verbose_name='نوع ملک')
    publish                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ انتشار')
    created                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ ثبت آگهی')
    updated                        = models.DateTimeField(default=timezone.now, verbose_name='تاریخ آپدیت آگهی')
    status                         = models.BooleanField(default=False, verbose_name='وضعیت تایید')
    code_domain                    = models.IntegerField(default=0, verbose_name='کد ملک')
    for_exchange                   = models.BooleanField(default=False, verbose_name='معاوضه')
