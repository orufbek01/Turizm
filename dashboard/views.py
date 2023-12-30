from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, UpdateAPIView, DestroyAPIView
from main.models import *
from main.serializers import *


class CreateEmployee(ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class UpdateEmployee(UpdateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class CreateGit(ListCreateAPIView):
    queryset = Linguist.objects.all()
    serializer_class = LinguistSerializer


class UpdateGit(UpdateAPIView):
    queryset = Linguist.objects.all()
    serializer_class = LinguistSerializer


class DeleteGit(DestroyAPIView):
    queryset = Linguist.objects.all()
    serializer_class = LinguistSerializer


class CreateHotel(ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class UpdateHotel(UpdateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class DeleteHotel(DestroyAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class CreateRestorant(ListCreateAPIView):
    queryset = Restorant.objects.all()
    serializer_class = RestaurantSerializer


class UpdateRestorant(UpdateAPIView):
    queryset = Restorant.objects.all()
    serializer_class = RestaurantSerializer


class DeleteRestorant(DestroyAPIView):
    queryset = Restorant.objects.all()
    serializer_class = RestaurantSerializer


class CreateWorkplace(ListCreateAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class UpdateWorkplace(UpdateAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class DeleteWorkplace(DestroyAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class CreateAddress(ListCreateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class UpdateAddress(UpdateAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class DeleteAddress(DestroyAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class CreateSubCategoryLocation(ListCreateAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class UpdateSubCategoryLocation(UpdateAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class DeleteSubCategoryLocation(DestroyAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class CreateOrder(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class UpdateOrder(UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class DeleteOrder(DestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class CreateRating(ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class UpdateRating(UpdateAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class DeleteRating(DestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class CreateCategory(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UpdateCategory(UpdateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class DeleteCategory(DestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CreateMenu(ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class UpdateMenu(UpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class DeleteMenu(DestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class CreateFoodOrder(ListCreateAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer


class UpdateFoodOrder(UpdateAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer


class DeleteFoodOrder(DestroyAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer


class CreateOrderTable(ListCreateAPIView):
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer


class UpdateOrderTable(UpdateAPIView):
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer


class DeleteOrderTable(DestroyAPIView):
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer






