from django.contrib.auth.decorators import login_required
from django.http import HttpRequest, JsonResponse, Http404
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.views import View
from django.views.generic import TemplateView, ListView

from account_module.models import MyUser, UserTicket, Announcements, MessageBox
from order_module.models import Order, OrderDetail, DiscountCode
from services_module.models import TablePricesRows
from .forms import EditProfileModelForm, UserTicketForm
from django.utils.decorators import method_decorator


# Create your views here.

@method_decorator(login_required, name='dispatch')
class UserPanelDashboardView(TemplateView):
    template_name = 'user_panel_module/user_panel_dashboard_page.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        order: Order = Order.objects.filter(is_paid=True, user_id=self.request.user.id).order_by('-payment_date')[:3]
        context['orders'] = order
        return context


@method_decorator(login_required, name='dispatch')
class EditUserProfilePage(View):
    def get(self, request: HttpRequest):
        current_user = MyUser.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(initial={
            'first_name': current_user.first_name,
            'last_name': current_user.last_name,
            'avatar': current_user.avatar
        })
        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)

    def post(self, request: HttpRequest):
        current_user: MyUser = MyUser.objects.filter(id=request.user.id).first()
        edit_form = EditProfileModelForm(request.POST, request.FILES, instance=current_user)
        if edit_form.is_valid():
            edit_form.save(commit=True)
            return render(request, 'user_panel_module/edit_profile_page.html', context={
                'form': edit_form,
                'success': 'اطلاعات شما با موفقیت تغییر پیدا کرد'
            })

        context = {
            'form': edit_form
        }
        return render(request, 'user_panel_module/edit_profile_page.html', context)


@login_required
def user_panel_menu_component(request):
    user_basket_count = OrderDetail.objects.filter(order__user_id=request.user.id, order__is_paid=False).count()
    discount_code_count = DiscountCode.objects.filter(user_id=request.user.id, is_active=True).count()
    user_paid_count = Order.objects.filter(is_paid=True, user_id=request.user.id).count()
    announcement_count = Announcements.objects.filter(is_active=True).count()
    message_count = MessageBox.objects.filter(is_active=True, user_id=request.user.id).count()

    context = {
        'user_basket_count': user_basket_count,
        'discount_code_count': discount_code_count,
        'user_paid_count': user_paid_count,
        'announcement_count': announcement_count,
        'message_count': message_count
    }
    return render(request, 'components/user_panel_menu_component.html', context)


@login_required
def user_panel_header_component(request):
    current_user: MyUser = MyUser.objects.filter(id=request.user.id).first()
    user_basket_count = OrderDetail.objects.filter(order__user_id=request.user.id, order__is_paid=False).count()
    discount_code_count = DiscountCode.objects.filter(user_id=request.user.id, is_active=True).count()
    user_paid_count = Order.objects.filter(is_paid=True, user_id=request.user.id).count()
    announcement_count = Announcements.objects.filter(is_active=True).count()
    message_count = MessageBox.objects.filter(is_active=True, user_id=request.user.id).count()

    context = {
        'current_user': current_user,
        'user_basket_count': user_basket_count,
        'discount_code_count': discount_code_count,
        'user_paid_count': user_paid_count,
        'announcement_count': announcement_count,
        'message_count': message_count
    }
    return render(request, 'components/user_panel_header_component.html', context)


@login_required
def user_basket(request: HttpRequest):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = 0

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_title and order_detail.package.discount_number:
            discount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount)
            package_instance.save()
            total_amount += int(discount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount,
    }
    return render(request, 'user_panel_module/user_basket.html', context)


@login_required
def remove_order_detail(request):
    detail_id = request.GET.get('detail_id')
    if detail_id is None:
        return JsonResponse({
            'status': 'not_found_detail_id'
        })
    deleted_count, deleted_dict = OrderDetail.objects.filter(id=detail_id, order__is_paid=False,
                                                             order__user_id=request.user.id).delete()

    if deleted_count == 0:
        return JsonResponse({
            'status': 'detail_not_found'
        })

    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = 0

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_title and order_detail.package.discount_number:
            discount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount)
            package_instance.save()
            total_amount += int(discount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount,
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


@login_required
def change_order_detail_count(request: HttpRequest):
    detail_id = request.GET.get('detail_id')
    state = request.GET.get('state')

    if detail_id is None or state is None:
        return JsonResponse({
            'status': 'not_found_detail_or_state'
        })

    order_detail = OrderDetail.objects.filter(id=detail_id, order__user_id=request.user.id,
                                              order__is_paid=False).first()
    if order_detail is None:
        return JsonResponse({
            'status': 'detail_not_found'
        })
    if state == 'increase':
        order_detail.count += 1
        order_detail.save()

    elif state == 'decrease':
        if order_detail.count == 1:
            order_detail.delete()
        else:
            order_detail.count -= 1
            order_detail.save()
    else:
        return JsonResponse({
            'status': 'state_invalid'
        })
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    total_amount = 0

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_title and order_detail.package.discount_number:
            discount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount)
            package_instance.save()
            total_amount += int(discount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    context = {
        'order': current_order,
        'sum': total_amount,
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


@login_required
def discount_code(request):
    discount: DiscountCode = DiscountCode.objects.filter(is_active=True, user=request.user.id).all()
    context = {
        'discount_codes': discount
    }
    return render(request, 'user_panel_module/user_panel_discount_page.html', context)


@login_required
def calculate_total_price_with_discount_code(request):
    current_order, created = Order.objects.prefetch_related('orderdetail_set').get_or_create(is_paid=False,
                                                                                             user_id=request.user.id)
    discount_code = request.GET.get('discount_value')

    request.session['discount_code'] = discount_code
    current_discount_codes = DiscountCode.objects.filter(is_active=True, user=request.user.id)
    total_price_with_discount_code = None
    discount_price = None
    total_amount = 0

    for order_detail in current_order.orderdetail_set.all():
        if order_detail.package.discount_title and order_detail.package.discount_number:
            discount = order_detail.package.price - (
                    order_detail.package.price * order_detail.package.discount_number / 100)
            package_instance: TablePricesRows = TablePricesRows.objects.filter(id=order_detail.package_id).first()
            package_instance.discount_price = int(discount)
            package_instance.save()
            total_amount += int(discount) * order_detail.count
        else:
            total_amount += order_detail.package.price * order_detail.count

    if current_discount_codes is not None:
        for code_value in current_discount_codes:
            if code_value.code == discount_code:
                total_price_with_discount_code = int(total_amount - (total_amount * code_value.amount / 100))
                discount_price = int(total_amount * code_value.amount / 100)

    context = {
        'order': current_order,
        'sum': total_amount,
        'total_price_with_discount_code': total_price_with_discount_code,
        'discount_price': discount_price
    }
    data = render_to_string('user_panel_module/user_basket_content.html', context)
    return JsonResponse({
        'status': 'success',
        'body': data
    })


@method_decorator(login_required, name='dispatch')
class UserPaidShoppingView(ListView):
    model = Order
    template_name = 'user_panel_module/user_paid_shopping.html'
    paginate_by = 5
    ordering = ['-payment_date']

    def get_queryset(self):
        queryset = super().get_queryset()
        request: HttpRequest = self.request
        queryset = queryset.filter(user_id=request.user.id, is_paid=True)
        return queryset


@login_required
def user_paid_shopping_details(request, order_id):
    order: Order = Order.objects.prefetch_related('orderdetail_set').filter(is_paid=True, id=order_id,
                                                                            user_id=request.user.id).first()
    context = {
        'order': order
    }
    return render(request, 'user_panel_module/user_detail_paid_shopping.html', context)


@method_decorator(login_required, name='dispatch')
class UserTicketView(View):
    def get(self, request):
        ticket_form = UserTicketForm()
        context = {
            'ticket_form': ticket_form
        }
        return render(request, 'user_panel_module/user_ticket_page.html', context)

    def post(self, request):
        ticket_form: UserTicketForm = UserTicketForm(request.POST, request.FILES)
        if ticket_form.is_valid():
            new_ticket = UserTicket(
                user_id=self.request.user.id,
                subject=ticket_form.cleaned_data.get('subject'),
                text=ticket_form.cleaned_data.get('text'),
                image=ticket_form.cleaned_data.get('image'),
            )
            new_ticket.save()
            return render(request, 'user_panel_module/user_ticket_page.html', context={
                'success': 'تیکت شما با موفقیت ارسال گردید. و نتیجه به زودی از قسمت پیام ها به شما اطلاع‌رسانی خواهد شد.',
                'ticket_form': ticket_form})
        else:
            context = {
                'ticket_form': ticket_form
            }
            return render(request, 'user_panel_module/user_ticket_page.html', context)


@method_decorator(login_required, name='dispatch')
class AnnouncementsView(ListView):
    model = Announcements
    template_name = 'user_panel_module/Announcements.html'
    ordering = ['-created_date']
    context_object_name = 'announcements'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True)
        return queryset


@method_decorator(login_required, name='dispatch')
class MessageBoxView(ListView):
    model = MessageBox
    template_name = 'user_panel_module/message_box.html'
    ordering = ['-created_date']
    context_object_name = 'messages'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(is_active=True, user_id=self.request.user.id)
        return queryset
