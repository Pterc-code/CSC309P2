from rest_framework import serializers, status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('user', 'reservation')


class NotificationsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notification = get_object_or_404(Notification)
        serializer = NotificationSerializer(notification)
        Response(serializer.data)


class NotificationClearView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, id):
        notification = get_object_or_404(Notification, id=id)
        notification.is_cleared = True
        notification.save()
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)

class NotificationIDView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        notification = get_object_or_404(Notification, id=id)
        serializer = NotificationSerializer(notification)
        return Response(serializer.data)
