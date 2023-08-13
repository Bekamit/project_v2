from django.db import models


# Create your models here.


class Services(models.Model):
    service = models.CharField(max_length=250)

    img = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()

    def __str__(self):
        return self.service


class UnderService(models.Model):
    title = models.CharField(max_length=250)
    description = models.TextField()
    price = models.PositiveIntegerField()
    service = models.ForeignKey(Services, on_delete=models.CASCADE, related_name="under_services")

    img = models.ImageField()
    img2 = models.ImageField()
    img3 = models.ImageField()
    img4 = models.ImageField()

    def __str__(self):
        return self.title



class SelectCategory(models.Model):
    select_category = models.ForeignKey(Services, on_delete=models.CASCADE)

    def __str__(self):
        return self.select_category


class Booking_s(models.Model):
    under_service = models.ForeignKey(UnderService, on_delete=models.CASCADE)
    check_in_date = models.DateTimeField()
    check_out_date = models.DateTimeField()










