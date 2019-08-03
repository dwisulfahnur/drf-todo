from django.utils import timezone
from rest_framework import viewsets, status, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ToDoSerializer
from .models import ToDo


class ToDoViewSet(viewsets.ModelViewSet):
    serializer_class = ToDoSerializer
    page_size_query_param = 'page_size'
    max_page_size = 100
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return ToDo.objects.filter(user=self.request.user)

    @action(detail=True, methods=['post'])
    def set_as_complete(self, request, pk=None):
        todo = self.get_object()
        todo.completed_at = timezone.now()

        serializer = self.get_serializer(todo)
        return Response(serializer.data, status.HTTP_200_OK)

    def perform_create(self, serializer):
        serializer.save(user_id=self.request.user.id)
