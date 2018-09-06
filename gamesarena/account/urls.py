from django.urls import path
from . import views

# The urls of the account app

urlpatterns = [
    #login view
    path('login/', views.user_login, name='login')
]