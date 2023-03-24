from django.urls import path
from . import views
from .views import RegisterView, LoginView, LogoutView, ProfileView

app_name = 'account'
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name="logout"),
    path('view/', ProfileView.as_view(), name="profile"),
    # path('login', views.LoginAPIView.as_view(), name="login"),
    # path('viewprofile', views.UserDetailAPI.as_view(), name="viewprofile"),
    # path('editprofile', views.EditProfileAPIView.as_view(), name="editprofile"),
]
