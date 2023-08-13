
from rest_framework import serializers

from .models import SelectCategory, Services, UnderService, Booking_s

from drf_writable_nested.serializers import WritableNestedModelSerializer


class ServicesWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Services
        fields = '__all__'


class UnderSerializer(serializers.ModelSerializer):
    class Meta:
        model = UnderService
        fields = '__all__'


class ServicesReadSerializer(WritableNestedModelSerializer):
    under_services = UnderSerializer(many=True)
    class Meta:
        model = Services
        fields = '__all__'







class SelectReadSerializer(serializers.ModelSerializer):
    select_category = ServicesReadSerializer()
    class Meta:
        model = SelectCategory
        fields = '__all__'

class SelectWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = SelectCategory
        fields = '__all__'



class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking_s
        fields = '__all__'

class BookingReadSerializer(serializers.ModelSerializer):
    under_service = UnderSerializer()
    class Meta:
        model = Booking_s
        fields = '__all__'