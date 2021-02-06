from django.urls import path
from .views import sign_up

urlpatterns = [
    path('signup/', sign_up, name="signup"),
    
]