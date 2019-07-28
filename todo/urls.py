from rest_framework import routers
from .api import ToDoViewSet

app_name = 'todo-api'

router = routers.SimpleRouter()
router.register('todos', ToDoViewSet, basename='todo')

urlpatterns = router.urls
