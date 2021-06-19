from rest_framework import serializers
from .models import Buy, Rent, Image
from User.models import User



class BuySerializers(serializers.ModelSerializer):
    class Meta:
        model = Buy
        fields = '__all__'


class RentSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'

class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'






class BuyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializers()
        model = Buy
        fields = [
                'country',
                'city',
                'zone',
                'ghadr_o_sahm',
                'price',
                'area',
                'number_of_rooms',
                'age_of_house',
                'parking',
                'warehouse',
                'elevator',
                'balcony',
                'floors',
                'noumber_of_house_in_each_floor',
                'description',
                'images',
                'yard',
                'area_of_ground',
                'type_house',
                'code_domain',
                'for_exchange',
            ]


class ImageSerialize(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'


class RentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        user = UserSerializers()
        images = ImageSerialize()
        model = Rent
        fields = [
                'country',
                'city',
                'zone',
                'mortgage',
                'rent',
                'area',
                'number_of_rooms',
                'age_of_house',
                'parking',
                'warehouse',
                'elevator',
                'balcony',
                'floors',
                'noumber_of_house_in_each_floor',
                'description',
                'yard',
                'area_of_ground',
                'type_house',
                'code_domain',
            ]