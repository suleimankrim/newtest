from django.urls import path

from knox.views import LogoutView

from .views import UserAPIView, RegisterAPIView, LoginAPIView,UserFind

urlpatterns = [
    path('user', UserAPIView.as_view()),
    path('friend', UserFind.as_view()),
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('logout', LogoutView.as_view(), name='knox_logout'),

]
