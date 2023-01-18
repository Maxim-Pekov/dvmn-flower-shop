from django.db import models


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


class Order(models.Model):
    customer = models.CharField('Заказчик', max_length=100, unique=True)
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
        verbose_name='Специалист'
    )
    courier = models.ForeignKey(
        Courier,
        related_name='orders',
        verbose_name='Курьер',
        null=True,
        blank=True
    )
    adress = models.CharField('Адрес', max_length=200, null=True, blank=True)
    phone = models.CharField('Телефон', max_length=200, null=True, blank=True)
    time = models.DateTimeField('Дата и время доставки', null=True, blank=True)

    def __str__(self):
        return self.profile.name, self.bouquet.title

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'


class Consultation(models.Model):
    customer = models.CharField('Заказчик', max_length=100, unique=True)
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
