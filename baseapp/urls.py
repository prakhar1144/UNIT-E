from django.urls import path
from .views import home, result, mess, newsfeed, notice, contributor

urlpatterns = [
    path('', home, name="home"),
    path('result/<email>/', result, name="result"),
    path('mess/<email>/', mess, name="mess"),
    path('newsfeed/', newsfeed, name="newsfeed"),
    path('notice/', notice, name="notice"),
    path('contributor/', contributor, name="contributor")
]
