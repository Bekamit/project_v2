from django.contrib import admin

from account.models import CustomUser
from hotel.models import Hotel, Equipment, Room, Amenity, Booking, Comment

admin.site.register(CustomUser)
admin.site.register(Hotel)

admin.site.register(Equipment)
admin.site.register(Room)
admin.site.register(Amenity)
admin.site.register(Booking)
admin.site.register(Comment)