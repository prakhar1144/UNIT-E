from django.urls import path
from .views import home, result, mess, newsfeed, notice, contributor, routine

urlpatterns = [
    path('', home, name="home"),
    path('result/<email>/', result, name="result"),
    path('mess/<email>/', mess, name="mess"),
    path('routine/<email>/', routine, name="routine"),
    path('newsfeed/', newsfeed, name="newsfeed"),
    path('notice/', notice, name="notice"),
    path('contributor/', contributor, name="contributor")
]
