from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.urls import path, reverse_lazy

from users.apps import UsersConfig
from users.views import UserLoginView, UserLogoutView, UserRegisterView, UserUpdateView, activate_new_user

app_name = UsersConfig.name

urlpatterns = [
    path('login/', UserLoginView.as_view(), name='login'),  # авторизация пользователя
    path('logout/', UserLogoutView.as_view(), name='logout'),  # выход из системы
    path('register/', UserRegisterView.as_view(), name='register'),  # регистрация пользователя
    path('profile/', UserUpdateView.as_view(), name='profile'),  # изменения данных пользователя
    path('activate/<int:pk>/', activate_new_user, name='activate'),  # активация пользователя
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change_form.html', success_url=reverse_lazy('users:password_change_done')), name='change_password'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
]