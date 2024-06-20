from django.urls import path
from .views import *



urlpatterns = [
    path('signup/', signup, name='signup'),
    # path('google/', GoogleLoginView.as_view(), name='google'),
    path('register/', SignupView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('signin/', loggin, name='login'),
    path('reset-password/', reset_password, name='reset-password'),
    path('logout/', logout, name='logout'),
]