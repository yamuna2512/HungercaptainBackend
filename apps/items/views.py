from django.shortcuts import render
from django.shortcuts import render
from rest_framework import generics, filters
from .serializers import ItemSerializer
from django_filters.rest_framework import DjangoFilterBackend
from .models import Item


class ItemList(generics.ListAPIView):
    queryset = Item.objects.order_by('-created_at').filter(status='active')
    serializer_class = ItemSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name']

def get_queryset(self):
        queryset = Item.objects.filter(status='active').order_by('-created_at')
        category = self.request.query_params.get('category')

        # ✅ If category is not "all" and not empty, filter it
        if category and category != 'all':
            queryset = queryset.filter(category__iexact=category)
        return queryset