from rest_framework import serializers
from sale_order.models import ChairPost, ShowTimePost

class ChairPostSerializers(serializers.ModelSerializer):
    class Meta:
        model = ChairPost
        fields = ['pk' ,'type_chair', 'price', 'status']
    def save(self):
        try:
            chair_post = ChairPost(
                type_chair = self.validated_data['type_chair'],
                price = self.validated_data['price'],
                status = self.validated_data['status']
            )
            chair_post.save()
            return chair_post
        except KeyError:
            return serializers.ValidationError({'msg':'You must have a type chair, price, status'})

class ShowTimePostCreateSerializers(serializers.ModelSerializer):
    class Meta:
        model = ShowTimePost
        fields = ['pk','chair', 'film', 'total_price', 'amount_chair', 'time_show']
    
    def save(self):
        try:
            show_time = ShowTimePost(
                film = self.validated_data['film'],
                total_price = self.validated_data['total_price'],
                amount_chair = self.validated_data['amount_chair'],
                time_show = self.validated_data['time_show']
            )
            show_time.save()
            return show_time
        except KeyError:
            raise serializers.ValidationError({'msg':'You must have a film, total price, amount chair, time show.'})

    