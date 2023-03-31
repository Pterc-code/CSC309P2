from django.urls import path
from . import views
from .views import NotificationsView, NotificationClearView, NotificationIDView
app_name = 'notification'
urlpatterns = [
    path('notification/view', NotificationsView.as_view(), name='notificationView'),
    path('notification/clear', NotificationClearView.as_view(), name='notificationClearView'),
    path('notification/view/<int:pk>', NotificationIDView.as_view(), name='notificationIDView'),
]