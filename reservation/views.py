from django.shortcuts import render
from .models import Reservation
from property.models import Property
from rest_framework import serializers, generics, status
from rest_framework.response import Response
# Create your views here.

# reservation status macro code
PENDING, DENIED, EXPIRED, APPROVED, CANCEL_PENDING, CANCELED, TERMINATED, COMPLETED = 1, 2, 3, 4, 5, 6, 7, 8


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = ['property', 'user', 'start_date', 'end_date', 'status']

    def create(self, validated_data):
        instance = self.Meta.model(**validated_data)
        instance.save()
        return instance


class ReservationView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def post(self, request, property_id, *args, **kwargs):
        try:
            property = Property.objects.get(id=property_id)
        except Property.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        request.data['property'] = property
        request.data['user'] = request.user.id
        request.data['start_date'] = request.data.get('start_date', None)
        request.data['end_date'] = request.data.get('end_date', None)
        request.data['status'] = 1

        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            reservation = serializer.save()
            return Response(ReservationSerializer(reservation).data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = self.serializer_class(reservation)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ReservationStatusDeniedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = DENIED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusExpiredView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = EXPIRED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusApprovedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = APPROVED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusCancelRequestView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = CANCEL_PENDING
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusCancelDeniedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # cancel request denied -> approved
        reservation.status = APPROVED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusCancelApprovedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # cancel request approved -> canceled
        reservation.status = CANCELED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusTerminatedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = TERMINATED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)


class ReservationStatusCompletedView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    lookup_field = 'id'

    def update(self, request, *args, **kwargs):
        try:
            reservation_id = kwargs['id']
            reservation = Reservation.objects.get(id=reservation_id)
        except Reservation.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        reservation.status = COMPLETED
        reservation.save()

        serializers = self.serializer_class(reservation)
        return Response(serializers.data, status=status.HTTP_200_OK)
