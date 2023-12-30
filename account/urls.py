from django.urls import path
from .views import *


urlpatterns = [
    path('sign_up/', singup_view),
    path('sign_in/', singin_view),
    path('update_user', UpdateUser.as_view())
]