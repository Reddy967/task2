from django.urls import path, include
from .views import getPhoneNumberRegistered, getPhoneNumberRegistered_TimeBased
from .views import RegisterAPI
from knox import views as knox_views
from .views import LoginAPI

urlpatterns = [
    path('<phone>/', getPhoneNumberRegistered.as_view(), name="OTP Gen"),
    path("time_based/<phone>/", getPhoneNumberRegistered_TimeBased.as_view(), name="OTP Gen Time Based"),
    path('', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
]