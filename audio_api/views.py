from rest_framework import viewsets
from rest_framework.response import Response
from .models import AudioElement
from .serializers import AudioElementSerializer
from rest_framework import status
 
class AudioElementViewSet(viewsets.ModelViewSet):
    queryset = AudioElement.objects.all()
    serializer_class = AudioElementSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def get_queryset(self):
        start_time = self.request.query_params.get('start_time')
        end_time = self.request.query_params.get('end_time')
        queryset = super().get_queryset()
        if start_time is not None and end_time is not None:
            queryset = queryset.filter(start_time__gte=start_time, end_time__lte=end_time)
        return queryset


