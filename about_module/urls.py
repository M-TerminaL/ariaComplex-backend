from django.urls import path
from . import views

urlpatterns = [
    path('about-us', views.AboutUsView.as_view(), name="about_us_page")
]