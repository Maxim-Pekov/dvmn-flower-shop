from django.db import models
from django.contrib.auth.models import User


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

    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='profilies',
        verbose_name='Пользователь'
    )
    adress = models.CharField('Адрес', max_length=200, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=200)
    email = models.CharField('Емайл', max_length=200, null=True, blank=True)

    def __str__(self):
        return self.user.username

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'


class Specialist(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    vacation = models.DateField('Даты отпуска')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специалист'
        verbose_name_plural = 'Специалисты'


class Courier(models.Model):
    name = models.CharField('Имя', max_length=100, unique=True)
    vacation = models.DateField('Даты отпуска')

    def __str__(self):
        return self.name


class Order(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Профиль',
    )
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
    )
    courier = models.ForeignKey(
        Courier,
        related_name='orders',
        verbose_name='Курьер',
    )

    def __str__(self):
        return self.profile.name, self.bouquet.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Delivery(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='deliveries',
        verbose_name='Профиль',
    )
    bouquet = models.ForeignKey(
        Bouquet,
        on_delete=models.CASCADE,
        related_name='deliveries',
        verbose_name='Букет',
    )
    delivery_at = models.DateTimeField('Дата и время формирования доставки', auto_now=True)
    courier = models.ForeignKey(
        Courier,
        on_delete=models.CASCADE,
        related_name='deliveries',
        verbose_name='Курьер',
    )
    adress = models.CharField('Адрес доставки', max_length=100)
    telephone = models.CharField('Номер телефона', max_length=100)
    time = models.DateTimeField('Дата и время доставки')

    def __str__(self):
        return self.profile.name, self.bouquet.title

    class Meta:
        verbose_name = 'Доставка'
        verbose_name_plural = 'Доставки'


class Consultation(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name='consultations',
        verbose_name='Профиль',
    )
    specialist = models.ForeignKey(
        Specialist,
        on_delete=models.CASCADE,
        related_name='consultations',
        verbose_name='Специалист',
    )
    time_at = models.DateTimeField('Дата и время формирования консультации', auto_now=True)
    time_finish = models.DateTimeField('Дата и время окончания консультации')

    def __str__(self):
        return self.profile.user.username, self.specialist.name

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
