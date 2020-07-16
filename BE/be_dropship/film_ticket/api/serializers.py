from rest_framework import serializers
from film_ticket.models import Chair, Room
from film.models import FilmPost

class ChairSerialzers(serializers.ModelSerializer):
    class Meta:
        model = Chair
        fields = ['pk','status', 'price']

class RoomCreateSerializers(serializers.ModelSerializer):   
    chairs = ChairSerialzers(many=True)
    class Meta:
        model = Room
        fields = ['pk', 'chairs', 'film', 'date_show']
    def create(self, validated_data):
        chairs_data = validated_data.pop('chairs')
        room = Room.objects.create(**validated_data)
        for chair_data in chairs_data:
            Chair.objects.create(room=room,**chair_data)
        return room

class RoomUpdateSerializers(serializers.ModelSerializer):
    chairs = ChairSerialzers(many=True)
    class Meta:
        model = Room
        fields = ['chairs', 'film', 'date_show']
        








        