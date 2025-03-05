from . import views
from django.urls import path

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register_page'),
    path('login/', views.LoginView.as_view(), name="login_page"),
    path('activate-account/', views.ActivateAccountView.as_view(), name="activate_account_page"),
    path('otp-pass-verify/', views.LoginSmsPassView.as_view(), name="login_sms_pass_page"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
]