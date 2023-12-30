from .models import *
from main.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = User
        fields = "__all__"


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Hotel
        fields = "__all__"


class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 4
        model = Restorant
        fields = "__all__"


class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Employee
        fields = "__all__"


class WorkplaceSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Workplace
        fields = "__all__"

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Order
        fields = "__all__"


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Report
        fields = "__all__"


class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 2
        model = Rating
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Menu
        fields = "__all__"


class FoodOrderSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = FoodOrder
        fields = "__all__"


class OrderTableSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = OrderTable
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Address
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Category
        fields = "__all__"


class SubCategoryLocationSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = SubCategoryLocation
        fields = "__all__"


class TableNumberSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Table_number
        fields = "__all__"


class LinguistSerializer(serializers.ModelSerializer):
    class Meta:
        depth = 3
        model = Linguist
        fields = "__all__"


