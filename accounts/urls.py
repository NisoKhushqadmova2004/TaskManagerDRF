from django.urls import path
from .views import register_view, users_list, LoginView, logout_view

urlpatterns = [
    path('register/', register_view),
    path('users/', users_list),
    path('login/', LoginView.as_view()),
    path('logout/', logout_view),
]