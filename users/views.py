import secrets

from django.core.mail import send_mail
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic.edit import CreateView, UpdateView

from config.settings import EMAIL_HOST_USER
from .models import User
from .forms import CustomUserCreationForm, ProfileUpdateForm

from django.contrib.auth.mixins import LoginRequiredMixin


class RegisterView(CreateView):
    model = User
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('catalog:product_list')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        user = form.save(commit=False)
        user.is_active = False
        user.token = secrets.token_hex(16)
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{user.token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Привет! Перейди по ссылке для подтверждения почты: {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.token = None
    user.save()
    return redirect(reverse("users:login"))


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = ProfileUpdateForm
    template_name = 'profile.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return self.request.user
