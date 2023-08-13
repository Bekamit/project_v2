from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import RegisterView, LoginView, UserListView, RegistrationPhoneView, VerifyEmail

urlpatterns = [
    path('registration/', RegisterView.as_view()),
    path('register-phone/', RegistrationPhoneView.as_view()),
    # path('activate/', ActivationView.as_view()),
    path('login/', LoginView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('', UserListView.as_view()),
    path('email-verify', VerifyEmail.as_view(), name='email-verify')
]