from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Bouquet(models.Model):
    title = models.CharField('Название', max_length=200, unique=True)
    price = models.DecimalField('Цена', max_digits=10, decimal_places=2)
    description = models.TextField(
        'Описание',
        blank=True,
        null=True
    )
    image = models.ImageField(upload_to='bouquet_images/', blank=True)
    flowers = models.ManyToManyField(
        'Flower',
        related_name='bouquet_flowers',
        verbose_name='Цветы'
    )
    Categories = models.ForeignKey(
        Category,
        related_name='bouquets',
        verbose_name='Категории',
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']
        verbose_name = 'Букет'
        verbose_name_plural = 'Букеты'


class Flower(models.Model):
    title = models.CharField('Название', max_length=100, unique=True)
    count_flower = models.PositiveSmallIntegerField('Кол-во в букете')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Цветок'
        verbose_name_plural = 'Цветы'


class Specialist(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    vacation = models.DateField('Даты отпуска', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Courier(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    vacation = models.DateField('Даты отпуска', null=True, blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Курьер'
        verbose_name_plural = 'Курьеры'


class Order(models.Model):
    customer = models.CharField('Заказчик', max_length=100,)
    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Букет'
    )
    time_at = models.DateTimeField('Дата и время заказа', auto_now=True)
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Специалист',
        null=True,
        blank=True,
    )
    courier = models.ForeignKey(
        Courier,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Курьер',
        null=True,
        blank=True
    )
    address = models.CharField('Адрес', max_length=200, null=True, blank=True)
    phone = PhoneNumberField('Телефон', db_index=True)
    delievry_date = models.DateTimeField('Дата и время доставки', null=True, blank=True)
    is_paid = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    payment_id = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'Заказ №{self.pk} - {self.customer} - {self.bouquet.title}'

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Consultation(models.Model):
    customer = models.CharField('Заказчик', max_length=100)
    phone = PhoneNumberField('Телефон', db_index=True)

    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        related_name='consultations',
        verbose_name='Специалист',
        null=True,
    )
    time_at = models.DateTimeField('Дата и время формирования консультации', auto_now=True)
    time_finish = models.DateTimeField('Дата и время окончания консультации', null=True)

    def __str__(self):
        return f'{self.customer}, {self.phone}'

    class Meta:
        verbose_name = 'Консультация'
        verbose_name_plural = 'Консультации'
