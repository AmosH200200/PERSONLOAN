from django.urls import path
from .views import *

urlpatterns=[
    path('login/', login_user, name="login-user"),
    path('register/', register, name="register-user"),
    path('logout/', logout_user, name="logout-user"),
    path('procedure/', procedure, name="procedure"),
]