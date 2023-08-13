from rest_framework import viewsets
from rest_framework.viewsets import generics, ModelViewSet
from rest_framework import permissions
from hotel.models import Hotel, Equipment, Room, Booking, Comment
from hotel.serializers import (

    HotelWriteSerializer,
    EquipmentSerializer,
    HotelRetrieveSerializer,
    HotelListSerializer, 
    BookingWriteSerializer, 
    BookingReadSerializer,
    CommentSerializer,
    RoomWriteSerializer
)

from rest_framework.permissions import IsAdminUser

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all
    serializer_class = RoomWriteSerializer

 
class HotelViewSet(viewsets.ModelViewSet):
    queryset = Hotel.objects.prefetch_related(
        'rooms__amenities__equipment',
        'rooms__type'
    ).order_by('pk')
    write_serializer_class = HotelWriteSerializer
    list_serializer_class = HotelListSerializer
    retrieve_serializer_class = HotelRetrieveSerializer
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        serializer_action_mapping = {
            'create': self.write_serializer_class,
            'retrieve': self.retrieve_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class,
        }
        return serializer_action_mapping.get(self.action, self.list_serializer_class)

class EquipmentViewSet(viewsets.ModelViewSet):
    queryset = Equipment.objects.order_by('pk')
    serializer_class = EquipmentSerializer
    permission_classes = [IsAdminUser]


class BookingViewSet(viewsets.ModelViewSet):
    queryset = Booking.objects.order_by('pk')
    write_serializer_class = BookingWriteSerializer
    read_serializer_class = BookingReadSerializer
    def get_serializer_class(self):
        serializer_action_mapping = {
            'create': self.write_serializer_class,
            'update': self.write_serializer_class,
            'partial_update': self.write_serializer_class,

        }

        return serializer_action_mapping.get(
            self.action,
            self.read_serializer_class
        )

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticated,)



class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'id'

    def get_permissions(self):
        if self.request.method == 'DELETE':
            return permissions.AllowAny(),
        return permissions.IsAuthenticated(),