
from django.urls import path
from . import views
from .views import LoginView, IndexView, RegisterView, SearchView

urlpatterns = [

    path('login/', LoginView.as_view(), name='login'),
    path('', IndexView.as_view(), name='index'),
    path('search/', SearchView.as_view(), name='search'),
    path('register/', RegisterView.as_view(), name='register'),


]




