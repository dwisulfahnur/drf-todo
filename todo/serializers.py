from rest_framework import serializers
from .models import ToDo


class ToDoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToDo
        fields = ('id', 'user_id', 'title', 'is_completed', 'completed_at', 'created_at', 'updated_at')
        extra_kwargs = {
            'completed_at': {'read_only': True},
            # 'user_id': {'read_only': True},
        }
