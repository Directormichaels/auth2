#Accounts/urls

from django.urls import path
from Account import views
from .views import SignUpView
urlpatterns = [
path('signup/', SignUpView.as_view(), name='signup'),
path('log/', views.LoginPage, name='loginpage')
]