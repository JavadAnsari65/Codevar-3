from django.urls import path

from .views import *

app_name = 'User'
urlpatterns = [
    path('Profile', Panel),
    path('Login-Create', LoginCreate, name='Login-Create'),
    path('Login/LoginCheck', LoginCheck),
    path('CreateAccount', CreateAccount),
    path('Profile/SubmitProject', SubmitProject),
    path('Profile/CancelProject', CancelProject),
    path('Profile/SubmitInfo', SubmitInfo),
    path('Profile/GetProject', GetProject),
]
