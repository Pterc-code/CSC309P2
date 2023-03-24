
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView

from .models import Property
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import django_filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('name', 'address', 'rating', 'description', 'price', 'bedroom', 'guest_allowed', 'bathroom', 'bed')


@api_view(['GET'])
def PropertyOverview(request):
    api_urls = {
        'all_items': '/',
        'Add': '/create',
        'Update': '/update/pk',
        'Delete': '/Property/delete/pk',
        'Create': '/Property/create/pk'
    }

    return Response(api_urls)


# Create
@api_view(['POST'])
def add_property(request):
    Property = PropertySerializer(data=request.data)

    if Property.is_valid():
        Property.save()
        return Response(Property.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


# View
@api_view(['GET'])
def view_property(request, pk):
    # checking for the parameters from the URL
    property = Property.objects.filter(pk__exact=pk)
    # if there is something in items else raise error
    if Property:
        serializer = PropertySerializer(property, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



# Update
@api_view(['POST'])
def update_property(request, pk):
    # property = Property.objects.filter(pk__exact=pk)
    property = get_object_or_404(Property, pk=pk)
    if property:
        data = PropertySerializer(instance=property, data=request.data)

        if data.is_valid():
            data.save()
            return Response(data.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
# Delete
@api_view(['DELETE'])
def delete_property(request, pk):
    property = get_object_or_404(Property, pk=pk)
    property.delete()
    return Response(status=status.HTTP_202_ACCEPTED)


# Search
@api_view(['GET'])
def search_property(request, name, rating, price, bedroom, order_by_price, order_by_rating):
    # checking for the parameters from the URL

    property = Property.objects.filter(name__icontains=name, rating__gte=rating, price__gte=price, bedroom__exact=bedroom).order_by(f'{order_by_price}', f'{order_by_rating}')

    # if there is something in items else raise error
    if Property:
        serializer = PropertySerializer(property, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)





