from django.db import models
from django.template.defaultfilters import slugify
import qrcode
from io import BytesIO
from django.core.files import File
from django.core.validators import RegexValidator
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    phone_number = models.CharField(max_length=13,blank=True, null=True, unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    git = models.ForeignKey(to='Git', on_delete=models.PROTECT, blank=True)


    class Meta:
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class SubCategoryLocation(models.Model):
    address = models.ForeignKey(to='Address', on_delete=models.CASCADE)


class Linguist(models.Model):
    guide = models.ForeignKey(to='User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55,)
    last_name = models.CharField(max_length=55,)
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam', unique=True, validators=[
            RegexValidator(
                regex='^[\+]9{2}8{1}[0-9]{9}$',
                message='Invalide phone number',
                code='Invalid number'
                )
    ])
    img = models.ImageField(upload_to='git_img/',)


class Restorant(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=55)
    restorant_bamk_number = models.PositiveIntegerField(null=True, blank=True)
    sub_category_location = models.ForeignKey(to='SubCategoryLocation', on_delete=models.PROTECT)
    category_location = models.ForeignKey(to='Address', on_delete=models.PROTECT)
    description = models.TextField()
    call_centre = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam', unique=True,validators=[
            RegexValidator(
                regex='^[\+]9{2}8{1}[0-9]{9}$',
                message='Invalide phone number',
                code='Invalid number'
        )
    ])


class Hotel(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.PROTECT)
    name = models.CharField(max_length=255)
    hotel_bank_number = models.PositiveIntegerField(null=True, blank=True)
    sub_category_location = models.ForeignKey(to='SubCategoryLocation', on_delete=models.PROTECT)
    category_location = models.ForeignKey(to='Address', on_delete=models.PROTECT)
    description = models.TextField(null=True, blank=True)
    call_centre = models.CharField(max_length=13, blank=True, null=True,verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    number_rooms = models.IntegerField(default=0)
    amenities = models.TextField()
    img = models.ImageField(upload_to='Hotel_img/')


class Employee(models.Model):
    user = models.ForeignKey(to='User', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=55, verbose_name='Ismingiz')
    last_name = models.CharField(max_length=55, verbose_name='Familyangiz')
    phone_number = models.CharField(max_length=13, blank=True, null=True,verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    workplace = models.ForeignKey(to='Workplace', on_delete=models.PROTECT, verbose_name='Ish_joyingiz')
    salary = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Oyligiz')
    age = models.IntegerField(default=15, verbose_name='Yoshingiz')
    start_work_time = models.TimeField()
    end_work_time = models.TimeField()
    rating = models.FloatField(default=0)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.first_name


class Workplace(models.Model):
    name = models.CharField(max_length=155, verbose_name='Ish_joyi')
    adress = models.ForeignKey(to='Address', on_delete=models.CASCADE, verbose_name='Manzil')

    def __str__(self):
            return self.name


class Address(models.Model):
    name = models.CharField(max_length=55, verbose_name='Manzil')

    def __str__(self):
       return self.name


class Order(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Ismingiz')
    last_name = models.CharField(max_length=55, verbose_name='Familyangiz')
    food = models.ManyToManyField(to='Menu', verbose_name='Taom_Tanlang')
    room = models.IntegerField(default=0)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.car_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)

        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)

        super().save(*args, **kwargs)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.first_name)
            super().save(*args, **kwargs)


class Report(models.Model):
     user = models.ForeignKey(to='User', on_delete=models.PROTECT)
     work_place = models.ForeignKey(to='Workplace', on_delete=models.PROTECT,verbose_name='Ish_joyi')
     problem = models.CharField(max_length=255, verbose_name='Muammo_sababi')
     slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)

     def save(self, *args, **kwargs):
        self.slug = slugify(self.work_place)
        super().save(*args, **kwargs)


class Rating(models.Model):
    work_place = models.ForeignKey(to='Workplace', on_delete=models.CASCADE, verbose_name='Ish_joyi')
    rating = models.FloatField(default=0, verbose_name='Baholang')


    def __str__(self):
        return self.rating


class Category(models.Model):
    name = models.CharField(max_length=155)

    def __str__(self):
        return self.name


class Menu(models.Model):
   name = models.CharField(max_length=55, verbose_name='Taom_nomi')
   catagory = models.ForeignKey(to='Category', on_delete=models.PROTECT, verbose_name='Turi')
   price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Narxi')
   img = models.ImageField(upload_to='menu_img/', verbose_name='Rasmi', null=True, blank=True)

   def __str__(self):
      return self.name


class FoodOrder(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Ismingiz')
    last_name = models.CharField(max_length=55, verbose_name='Familyangiz')
    food = models.ManyToManyField(to='Menu', verbose_name='Taom_nomi' )
    is_deliver = models.BooleanField(default=False, verbose_name='Yetkazib_berish_kerakmi')
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    extra_phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    PAYMENT_TYPE = (
        ('Karta', 'Karta'),
        ('Naqd pul', 'Naqd pul')
    )
    payment_type = models.CharField(max_length=55, choices=PAYMENT_TYPE)
    slug = models.SlugField(max_length=55, unique=True, blank=True, null=True)
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.phone_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.first_name)
        super().save(*args, **kwargs)


class Table_number(models.Model):
    number = models.IntegerField(default=1)


class OrderTable(models.Model):
    first_name = models.CharField(max_length=55, verbose_name='Ismingiz')
    last_name = models.CharField(max_length=55, verbose_name='Familyangiz')
    table_number = models.ForeignKey(to='Table_number', on_delete=models.PROTECT, verbose_name='Stol_raqami')
    food = models.ManyToManyField(to='Menu', blank=True, verbose_name='Taom_nomi')
    phone_number = models.CharField(max_length=13, blank=True, null=True,verbose_name='Telefon_raqam' , unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalide phone number',
            code='Invalid number'
        )
    ])
    qr_code = models.ImageField(upload_to='qr_codes/', blank=True, null=True)

    def save(self, *args, **kwargs):
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=8,
            border=4,
        )
        qr.add_data(f"Your data to encode in the QR code: {self.order.phone_number}")
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        buffer = BytesIO()
        img.save(buffer)
        buffer.seek(0)
        self.qr_code.save(f'qr_code_{self.id}.png', File(buffer), save=False)
        super().save(*args, **kwargs)











