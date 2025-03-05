from django.urls import path
from . import views

urlpatterns = [
    path('prices', views.PricesTableView.as_view(), name='prices-list'),
    path('<slug:slug>', views.services_detail, name='services-detail'),
]
