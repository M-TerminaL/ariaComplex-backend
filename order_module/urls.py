from . import views
from django.urls import path

urlpatterns = [
    path('add-to-order', views.add_package_to_order, name='add_package_to_order'),
    path('request-payment/', views.request_payment, name='request_payment'),
    path('verify-payment/', views.verify_payment, name='verify_payment')
]
