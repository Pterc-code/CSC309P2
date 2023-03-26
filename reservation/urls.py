from django.urls import path
from . import views

app_name = 'reservation'
urlpatterns = [
    path('<int:property_id>/reserve', views.ReservationView.as_view(), name='reserve'),
    path('<int:reservation_id>/view', views.ReservationView.as_view(), name='reservation_view'),
    path('<int:reservation_id>/denied',
         views.ReservationStatusDeniedView.as_view(), name='reservation_denied'),
    path('<int:reservation_id>/expired',
         views.ReservationStatusExpiredView.as_view(), name='reservation_expired'),
    path('<int:reservation_id>/approved',
         views.ReservationStatusApprovedView.as_view(), name='reservation_approved'),
    path('<int:reservation_id>/cancel_request',
         views.ReservationStatusCancelRequestView.as_view(), name='reservation_cancel_request'),
    path('<int:reservation_id>/cancel_request/denied',
         views.ReservationStatusCancelDeniedView.as_view(), name='reservation_cancel_denied'),
    path('<int:reservation_id>/cancel_request/approved',
         views.ReservationStatusCancelApprovedView.as_view(), name='reservation_cancel_approved'),
    path('<int:reservation_id>/terminated',
         views.ReservationStatusTerminatedView.as_view(), name='reservation_terminated'),
    path('<int:reservation_id>/completed',
         views.ReservationStatusCompletedView.as_view(), name='reservation_completed'),
]
