from rest_framework import viewsets, status
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from .models import Aircraft
from .serializers import AircraftSerializer
from airobjects.pagination import CustomLimitOffsetPagination

class AircraftViewSet(viewsets.ModelViewSet):
    serializer_class = AircraftSerializer
    pagination_class = CustomLimitOffsetPagination

    def get_queryset(self):
        return Aircraft.objects.all()

    def list(self, request):
        if 'limit' not in request.GET or 'offset' not in request.GET:
            return Response({'error': 'Both limit and offset parameters are required.'},
                            status=status.HTTP_400_BAD_REQUEST)

        filters = {param: value for param, value in request.GET.items() if param != 'offset' and param != 'limit'}
        queryset = self.get_queryset().filter(**filters)
        serializer = self.get_serializer(self.paginate_queryset(queryset=queryset), many=True)
        return self.get_paginated_response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            return Response({"uuid": instance.uuid}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        aircraft = get_object_or_404(self.queryset, uuid=pk)
        serializer = self.get_serializer(aircraft)
        return Response(serializer.data)

    def update(self, request, pk=None):
        aircraft = get_object_or_404(self.queryset, uuid=pk)
        serializer = self.get_serializer(aircraft, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        aircraft = get_object_or_404(self.queryset, uuid=pk)
        aircraft.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


