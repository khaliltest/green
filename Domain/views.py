from django.shortcuts import render
from .serializers import BuySerializers, RentSerializers, BuyCreateSerializer, RentCreateSerializer, ImageSerialize
from rest_framework import viewsets
from rest_framework import generics, filters
from .models import Buy, Rent, Image
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import rest_framework
from rest_framework.decorators import api_view
from .permisions import (
                        IsAdvisor,
                        IsAdvisorOrReadonly,
                        IsObjOwnerOrReadOnly,
                        IsOwner,
                        IsOwnerOrReadonly,
                        IsStaffOrReadonly,
                        IsSuperuser,
                    )
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser, IsAuthenticated
from rest_framework.authtoken.models import Token
# Create your views here.

class BuyFilter(rest_framework.FilterSet):
    min_price = rest_framework.NumberFilter(field_name="price", lookup_expr='gte')
    max_price = rest_framework.NumberFilter(field_name="price", lookup_expr='lte')
    min_area = rest_framework.NumberFilter(field_name="area", lookup_expr='gte')
    max_area = rest_framework.NumberFilter(field_name="area", lookup_expr='lte')
    min_rooms = rest_framework.NumberFilter(field_name="number_of_rooms", lookup_expr='gte')
    max_rooms = rest_framework.NumberFilter(field_name="number_of_rooms", lookup_expr='lte')
    class Meta:
        model = Buy
        fields = ['city', 'zone', 'min_price', 'max_price', 'min_rooms', 'max_rooms', 'user__is_owner', 'user__is_advisor']

class RentFilter(rest_framework.FilterSet):
    min_mortage = rest_framework.NumberFilter(field_name="mortgage", lookup_expr='gte')
    max_mortage = rest_framework.NumberFilter(field_name="mortgage", lookup_expr='lte')
    min_rent = rest_framework.NumberFilter(field_name="rent", lookup_expr='gte')
    max_rent = rest_framework.NumberFilter(field_name="rent", lookup_expr='lte')
    min_area = rest_framework.NumberFilter(field_name="area", lookup_expr='gte')
    max_area = rest_framework.NumberFilter(field_name="area", lookup_expr='lte')
    min_rooms = rest_framework.NumberFilter(field_name="number_of_rooms", lookup_expr='gte')
    max_rooms = rest_framework.NumberFilter(field_name="number_of_rooms", lookup_expr='lte')
    class Meta:
        model = Rent
        fields = ['city', 'zone', 'min_mortage', 'max_mortage', 'min_rent', 'max_rent', 'min_rooms', 'max_rooms', 'user__is_owner', 'user__is_advisor']

##############################################################################33


class BuyList(generics.ListAPIView):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = BuyFilter
    permission_classes = [IsAuthenticatedOrReadOnly,]
    ordering_fields = ['publish',]

class BuyDetail(generics.RetrieveAPIView):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    permission_classes = [IsAuthenticatedOrReadOnly,]


class BuyDelete(generics.DestroyAPIView):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = BuyFilter
    permission_classes = [IsObjOwnerOrReadOnly,]


class BuyUpdate(generics.UpdateAPIView):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = BuyFilter
    permission_classes = [IsObjOwnerOrReadOnly,]

class BuyCreate(generics.CreateAPIView):
    serializer_class = BuySerializers
    queryset = Buy.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = BuyFilter
    permission_classes = [IsAuthenticatedOrReadOnly,]
#####################################################################################

class RentList(generics.ListAPIView):
    serializer_class = RentSerializers
    queryset = Rent.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = RentFilter
    permission_classes = [IsAuthenticatedOrReadOnly,]
    ordering_fields = ['publish',]

class RentCreate(generics.CreateAPIView):
    serializer_class = RentSerializers
    queryset = Rent.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = RentFilter
    permission_classes = [IsObjOwnerOrReadOnly,]

class RentDetail(generics.RetrieveAPIView):
    serializer_class = RentSerializers
    queryset = Rent.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = RentFilter
    permission_classes = [IsAuthenticatedOrReadOnly,]

class RentDelete(generics.DestroyAPIView):
    serializer_class = RentSerializers
    queryset = Rent.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = RentFilter
    permission_classes = [IsObjOwnerOrReadOnly,]

class RentUpdate(generics.UpdateAPIView):
    serializer_class = RentSerializers
    queryset = Rent.objects.all()
    filter_backends = [filters.SearchFilter,DjangoFilterBackend]
    search_fields = ['user__number', 'code_domain']
    filterset_class = RentFilter
    permission_classes = [IsObjOwnerOrReadOnly,]


class ImageCreate(generics.CreateAPIView):
    serializer_class = ImageSerialize
    queryset = Image.objects.all()
    permission_classes = [IsObjOwnerOrReadOnly]





@api_view(['POST',])
def BuyCreate(request):
    if request.method == 'POST':
        serializer = BuyCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            buy  = serializer.save(user = request.user, code_domain = int('98'+id))
            data['response'] = "آگهی با موفقیت ساخته شد"
            data['country'] = buy.country
            data['city'] = buy.city
            data['zone'] = buy.zone
            data['ghadr_o_sahm'] = buy.ghadr_o_sahm
            data['price'] = buy.price
            data['area'] = buy.area
            data['number_of_rooms'] = buy.number_of_rooms
            data['age_of_house'] = buy.age_of_house
            data['parking'] = buy.parking
            data['warehouse'] = buy.warehouse
            data['elevator'] = buy.elevator
            data['balcony'] = buy.balcony
            data['floors'] = buy.floors
            data['noumber_of_house_in_each_floor'] = buy.noumber_of_house_in_each_floor
            data['description'] = buy.description
            data['yard'] = buy.yard
            data['area_of_ground'] = buy.area_of_ground
            data['type_house'] = buy.type_house
            data['code_domain'] = buy.code_domain
            data['for_exchange'] = buy.for_exchange
            data['owner'] = buy.user.id
        else:
            data = serializer.errors
        return Response(data)



@api_view(['POST',])
def RentCreate(request):
    if request.method == 'POST':
        serializer = RentCreateSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            buy  = serializer.save(user = request.user)
            data['response'] = "آگهی با موفقیت ساخته شد"
            data['country'] = buy.country
            data['city'] = buy.city
            data['zone'] = buy.zone
            data['mortgage'] = buy.mortgage
            data['rent'] = buy.rent
            data['area'] = buy.area
            data['number_of_rooms'] = buy.number_of_rooms
            data['age_of_house'] = buy.age_of_house
            data['parking'] = buy.parking
            data['warehouse'] = buy.warehouse
            data['elevator'] = buy.elevator
            data['balcony'] = buy.balcony
            data['floors'] = buy.floors
            data['noumber_of_house_in_each_floor'] = buy.noumber_of_house_in_each_floor
            data['description'] = buy.description
            data['yard'] = buy.yard
            data['area_of_ground'] = buy.area_of_ground
            data['type_house'] = buy.type_house
            data['code_domain'] = buy.code_domain
            
            data['owner'] = buy.user.id
        else:
            data = serializer.errors
        return Response(data)


@api_view(['GET',])
def HelpFront(request):
    data = {}
    data['کشور'] = 'فقط IR'
    data['شهر'] = 'TEH, ESF, MASH'
    data['کد منطقه'] = 'از ۱ تا ۲۲'

    return Response(data)



