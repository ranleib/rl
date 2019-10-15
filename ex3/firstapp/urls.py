from firstapp import views
from django.conf.urls import url

urlpatterns = [
    url(r'user/',views.users,name = 'users'),





]
