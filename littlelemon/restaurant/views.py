from django.shortcuts import render
from rest_framework import generics, viewsets, status # change to a detailed import?
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .serializers import MenuSerializer, BookingSerializer
from .models import Menu, Booking

# Create your views here.


def index(request):
  return render(request, 'index.html', {})


class MenuView(generics.ListCreateAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()


class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
  serializer_class = MenuSerializer
  queryset = Menu.objects.all()


class BookingViewSet(viewsets.ModelViewSet):
  serializer_class = BookingSerializer
  queryset = Booking.objects.all()
  permission_classes = [IsAuthenticated]
