from django.urls import path
from . import views # from this folder, import everything inside of "views"

urlpatterns = [
    path('users/', views.CustomUserList.as_view()),
    path('users/<int:pk>/', views.CustomUserDetail.as_view())
]