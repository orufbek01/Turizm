from django.shortcuts import render
from rest_framework.generics import ListAPIView, GenericAPIView
from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response


class GetHotel(ListAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelSerializer


class GetRestaurant(ListAPIView):
    queryset = Restorant.objects.all()
    serializer_class = RestaurantSerializer


class GetReport(ListAPIView):
    queryset = Report.objects.all()
    serializer_class = ReportSerializer


class GetGit(ListAPIView):
    queryset = Linguist.objects.all()
    serializer_class = LinguistSerializer


class GetRating(ListAPIView):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class GetWorkplace(ListAPIView):
    queryset = Workplace.objects.all()
    serializer_class = WorkplaceSerializer


class GetEmployee(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


class GetFoodOrder(ListAPIView):
    queryset = FoodOrder.objects.all()
    serializer_class = FoodOrderSerializer


class GetSubCategoryLocation(ListAPIView):
    queryset = SubCategoryLocation.objects.all()
    serializer_class = SubCategoryLocationSerializer


class GetCategory(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GetAddress(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer


class GetOrderTable(ListAPIView):
    queryset = OrderTable.objects.all()
    serializer_class = OrderTableSerializer


class GetMenu(ListAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class GetOrder(ListAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


@api_view(["GET"])
def hotel_by_name(request):
    name = request.GET.get("name")
    hotel = Hotel.objects.filter(name = name)
    ser = HotelSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def hotel_by_call_centre(request):
    call_centre = request.GET.get('call_centre')
    hotel = Hotel.objects.filter(call_centre = call_centre)
    ser = HotelSerializer(hotel, many=True)
    return Response(ser.data)


@api_view(['GET'])
def restorant_by_name(request):
    name = request.GET.get('name')
    restorant = Restorant.objects.filter(name = name)
    ser = RestaurantSerializer(restorant, many=True)
    return  Response(ser.data)


@api_view(['GET'])
def restorant_by_call_senter(request):
    call_centre = request.GET.get('call_centre')
    restorant = Restorant.objects.filter(call_centre=call_centre)
    ser = RestaurantSerializer(restorant, many=True)
    return Response(ser.data)


@api_view(['GET'])
def linguist_by_first_name(request):
    first_name = request.GET.get('firts_name')
    linguist = Linguist.objects.filter(first_name=first_name)
    ser = LinguistSerializer(linguist, many=True)
    return Response(ser.data)



@api_view(['GET'])
def linguist_by_last_name(request):
    first_name = request.GET.get('last_name')
    linguist = Linguist.objects.filter(last_name = last_name)
    ser = LinguistSerializer(linguist, many=True)
    return Response(ser.data)


@api_view(['GET'])
def linguist_by_phone_number(request):
    first_name = request.GET.get('phone_number')
    linguist = Linguist.objects.filter(phone_number = phone_number)
    ser = LinguistSerializer(linguist, many=True)
    return Response(ser.data)


@api_view(['GET'])
def employee_by_first_name(request):
    first_name = request.GET.get('first_name')
    employee = Employee.objects.filter(first_name = first_name)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def employee_by_last_name(request):
    last_name = request.GET.get('laast_name')
    employee = Employee.objects.filter(last_name = last_name)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)


@api_view(['GET'])
def employee_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    employee = Employee.objects.filter(phone_number = phone_number)
    ser = EmployeeSerializer(employee, many=True)
    return Response(ser.data)




@api_view(['GET'])
def employee_by_age(request):
    age = request.GET.get('age')
    employee = Employee.objects.filter(age = age)
    ser = EmployeeSerializer(employee,many=True)
    return Response(ser.data)


@api_view(['GET'])
def workplace_by_name(request):
    name = request.GET.get('name')
    workplace = Workplace.objects.filter(name = name)
    ser = WorkplaceSerializer(workplace,many=True)
    return Response(ser.data)



@api_view(['GET'])
def order_by_first_name(request):
    first_name = request.GET.get('first_name')
    order = Order.objects.filter(first_name = first_name)
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_by_last_name(request):
    last_name = request.GET.get('last_name')
    order = Order.objects.filter(last_name = last_name)
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_by_room(request):
    room = request.GET.get('room')
    order = Order.objects.filter(room = room)
    ser = OrderSerializer(order, many=True)
    return Response(ser.data)


@api_view(['GET'])
def address_by_name(request):
    name = request.GET.get('name')
    address = Address.objects.filter(name = name)
    ser = AddressSerializer(address, many=True)
    return Response(ser.data)


@api_view(['GET'])
def report_by_problem(request):
    problem = request.GET.get('problem')
    report = Report.objects.filter(problem =problem)
    ser = ReportSerializer(report, many=True)
    return Response(ser.data)


@api_view(['GET'])
def rating_by_work_place(request):
    work_place = request.GET.get('work_place')
    rating = Rating.objects.filter(work_place=work_place)
    ser = RatingSerializer(rating,many=True)
    return Response(ser.data)


@api_view(['GET'])
def category_by_name(request):
    name = request.GET.get('name')
    category = Category.objects.filter(name = name)
    ser = CategorySerializer(category, many=True)
    return Response(ser.data)


@api_view(['GET'])
def menu_by_name(request):
    name = request.GET.get('name')
    menu = Menu.objects.filter(name = name)
    ser = MenuSerializer(menu, many=True)
    return Response(ser.data)


@api_view(['GET'])
def menu_by_price(request):
    price = request.GET.get('price')
    menu = Menu.objects.filter(price = price)
    ser = MenuSerializer(menu, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_food_by_first_name(request):
    first_name = request.GET.get('first_name')
    order_food = FoodOrder.objects.filter(first_name = first_name)
    ser = FoodOrderSerializer(order_food, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_food_by_last_name(request):
    last_name = request.GET.get('last_name')
    order_food = FoodOrder.objects.filter(last_name = last_name)
    ser = FoodOrderSerializer(order_food, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_food_by_phone_number(request):
    phone_number = request.GET.get('phone_number')
    order_food = FoodOrder.objects.filter(phone_number = phone_number)
    ser = FoodOrderSerializer(order_food, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_food_by_extra_phone_number(request):
    extra_phone_number = request.GET.get('extra_phone_number')
    order_food = FoodOrder.objects.filter(extra_phone_number = extra_phone_number)
    ser = FoodOrderSerializer(order_food, many=True)
    return Response(ser.data)


@api_view(['GET'])
def table_number_by_number(request):
    number = request.GET.get('number')
    table_number = Table_number.objects.filter(number=number)
    ser = TableNumberSerializer(table_number, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_table_by_first_name(request):
    first_name = request.GET.get('first_name')
    order_table = OrderTable.objects.filter(first_name = first_name)
    ser = OrderTableSerializer(order_table, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_table_by_last_name(request):
    last_name = request.GET.get('last_name')
    order_table = OrderTable.objects.filter(last_name = last_name)
    ser = OrderTableSerializer(order_table, many=True)
    return Response(ser.data)


@api_view(['GET'])
def order_table_by_phone_number(request):
    phone_number =request.GET.get('phone_number')
    order_table = OrderTable.objects.filter(phone_number = phone_number)
    ser = OrderTableSerializer(order_table, many=True)
    return Response(ser.data)

