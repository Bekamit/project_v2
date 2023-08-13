from django.db import models
from account.models import CustomUser


# Create your models here.

class AbstractNameDescription(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField(blank=True)

    objects = models.Manager()

    class Meta:
        abstract = True

class Hotel(AbstractNameDescription):
    RATING = (
        ('1', '⭐️'),
        ('2', '⭐️⭐️'),
        ('3', '⭐️⭐️⭐️'),
        ('4', '⭐️⭐️⭐️⭐️'),
        ('5', '⭐️⭐️⭐️⭐️⭐️'),

    )
    category = models.CharField(max_length=250)
    image1 = models.ImageField()
    image2 = models.ImageField()
    image3 = models.ImageField()
    image4 = models.ImageField()
    rating = models.CharField(choices=RATING, max_length=250)


    class Meta:
        verbose_name = 'Отель'
        verbose_name_plural = 'Отель'


class Equipment(AbstractNameDescription):
    pass

    class Meta:
        verbose_name = 'Удобства'
        verbose_name_plural = 'Удобства'

class Room(models.Model):
    hotel = models.ForeignKey(
        'Hotel',
            on_delete=models.CASCADE,
            related_name='rooms'
    )
 
    equipments = models.ManyToManyField(
        'Equipment',
            related_name='rooms',
            through='Amenity',
            blank=True
    )
    title = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=9, decimal_places=2)
    is_available = models.BooleanField(default=True)

    guests = models.ManyToManyField(
        'account.CustomUser',
        related_name='rooms',
        through='Booking',
        blank=True)
    

    class Meta:
        verbose_name = 'Номер'
        verbose_name_plural = 'Номера'

    objects = models.Manager()

class Amenity(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='amenities')
    equipment = models.ForeignKey('Equipment', on_delete=models.CASCADE, related_name='amenities')
    quantity = models.PositiveSmallIntegerField()


    objects = models.Manager()

    class Meta:
        verbose_name = 'Условие'
        verbose_name_plural = 'Условии'

class Booking(models.Model):
    room = models.ForeignKey('Room', on_delete=models.CASCADE, related_name='bookings')
    guest = models.ForeignKey('account.CustomUser', on_delete=models.CASCADE, related_name='bookings')
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()


    objects = models.Manager()

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронировании'


class Comment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, related_name='rooms', on_delete=models.CASCADE, related_query_name='rooms')
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.user} commented {self.room}: {self.body}'
    
    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'