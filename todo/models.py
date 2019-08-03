from django.db import models
from django.contrib.auth import get_user_model


class ToDo(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    completed_at = models.DateTimeField("Completed At", null=True, blank=True)
    created_at = models.DateTimeField("Created Time", auto_now_add=True)
    updated_at = models.DateTimeField("Last Updated", auto_now=True)

    @property
    def is_completed(self):
        return (True if self.completed_at else False)
