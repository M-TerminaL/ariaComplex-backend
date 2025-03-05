from . import views
from django.urls import path

urlpatterns = [
    path('', views.UserPanelDashboardView.as_view(), name="user_panel_dashboard_page"),
    path('edit-profile', views.EditUserProfilePage.as_view(), name="edit_profile_page"),
    path('user-basket', views.user_basket, name='user_basket_page'),
    path('my-shopping', views.UserPaidShoppingView.as_view(), name='user_paid_shopping'),
    path('my-shopping-details/<order_id>', views.user_paid_shopping_details, name='user_paid_shopping_details'),
    path('remove-order-detail', views.remove_order_detail, name='remove_order_detail_ajax'),
    path('change-order-detail', views.change_order_detail_count, name='change_order_detail_count_ajax'),
    path('discount-codes', views.discount_code, name='discount_code_page'),
    path('calculate-discount-code', views.calculate_total_price_with_discount_code, name='calculate_total_price_with_discount_code'),
    path('user-ticket', views.UserTicketView.as_view(), name='user_ticket_page'),
    path('announcements', views.AnnouncementsView.as_view(), name='announcements_page'),
    path('messages', views.MessageBoxView.as_view(), name='message_box_page'),
]
