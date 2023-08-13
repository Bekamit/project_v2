from rest_framework import serializers


from account.serializers import GuestReadSerializer
from hotel.models import Hotel, Equipment, Room, Amenity, Booking, Comment

from drf_writable_nested.serializers import WritableNestedModelSerializer



class AmenityWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Amenity
        exclude = ['room']

class RoomWriteSerializer(WritableNestedModelSerializer):
    amenities = AmenityWriteSerializer(many=True)
    class Meta:
        model = Room
        exclude = ['hotel', 'equipments', 'guests']


class HotelWriteSerializer(WritableNestedModelSerializer):
    rooms = RoomWriteSerializer(many=True)
    class Meta:
        model = Hotel
        fields = '__all__'


class EquipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipment
        fields = '__all__'


class AmenityReadSerializer(AmenityWriteSerializer):
    equipment = EquipmentSerializer()





class RoomReadSerializer(RoomWriteSerializer):
    amenities = AmenityReadSerializer(many=True)



class HotelRetrieveSerializer(HotelWriteSerializer):
    rooms = RoomReadSerializer(many=True)


class HotelListSerializer(HotelRetrieveSerializer):
    rooms = None

class BookingWriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        exclude = ['guest']

    def validate_room(self, value):
        if not value.is_available:
            raise serializers.ValidationError('This room is not available')
        return value


    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['guest'] = request.user
        self.change_room_status(validated_data.get('room'))
        return super().create(validated_data)

    @staticmethod
    def change_room_status(room: Room) -> None:
        room.is_available = False
        room.save()


class BookingReadSerializer(serializers.ModelSerializer):
    room = RoomReadSerializer()
    guest = GuestReadSerializer()

    class Meta:
        model = Booking
        fields = '__all__'



class CommentSerializer(serializers.ModelSerializer):
    User = serializers.ReadOnlyField(source='user.id')
    User_username = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Comment
        fields = '__all__'

    def create(self, validated_data):
        product = self.context.get('room')
        product = Comment.objects.get(id=product.id)
        user = self.context.get('user')
        validated_data['user'] = user
        validated_data['room'] = product
        return super().create(validated_data)
