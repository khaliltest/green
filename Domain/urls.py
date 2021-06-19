from django.urls import path, include, re_path
from rest_framework import routers
from .views import (
                    #buy views
                    BuyList,
                    BuyDetail,
                    BuyDelete,
                    BuyUpdate,
                    BuyCreate,
                    #rent views
                    RentList,
                    RentUpdate,
                    RentCreate,
                    RentDelete,
                    RentDetail,
                    ImageCreate,
                    #front
                    HelpFront
            )


urlpatterns = [
    path('buy/list', BuyList.as_view(), name="‌buy-list"),
    path('buy/<int:pk>', BuyDetail.as_view(), name="‌buy-detail"),
    path('buy/<int:pk>/delete', BuyDelete.as_view(), name="‌buy-delete"),
    path('buy/<int:pk>/update', BuyUpdate.as_view(), name="‌buy-update"),
    path('buy/create', BuyCreate, name="‌buy-create"),
    ##################################################################
    path('rent/list', RentList.as_view(), name="‌rent-list"),
    path('rent/<int:pk>', RentDetail.as_view(), name="‌rent-detail"),
    path('rent/<int:pk>/delete', RentDelete.as_view(), name="‌rent-delete"),
    path('rent/<int:pk>/update', RentUpdate.as_view(), name="‌rent-update"),
    path('rent/create', RentCreate, name="‌rent-create"),
    ##################################################################
    path('Image/create', ImageCreate.as_view(), name="‌image-create"),
    ##################################################################
    path('help-front/', HelpFront, name='help-front')
]