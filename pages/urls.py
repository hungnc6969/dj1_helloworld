# pages/urls.py
# file nay mapping url den conten trong file views.py
from django.urls import path
from .views import homePageView


urlpatterns = [
    path('', homePageView, name = 'home'),
    ]


