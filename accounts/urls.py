from django.urls import path
from accounts.views import Usercreate
import django.contrib.auth.views as auth
urlpatterns = [
    path('login/',auth.LoginView.as_view(), name='login'),
    path('logout/',auth.LogoutView.as_view(), name='logout'),
    path('sign_up/',Usercreate.as_view(),name='sign_up'),
    path('password_change/',auth.PasswordChangeView.as_view(),name='password_change'),
    path('password_change_done/',auth.PasswordChangeDoneView.as_view(),name='password_change_done'),
    path('password_reset/',auth.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_done/',auth.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset/<uidb64>/<token>/',auth.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/',auth.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
    ]