from django.utils import timezone
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_queryset(self):
        return ToDo.objects.all()

    @action(detail=True, methods=['post'])
    def set_as_complete(self, request, pk=None):
        todo = self.get_object()
        todo.completed_at = timezone.now()

        serializer = self.get_serializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)
