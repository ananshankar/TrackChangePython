"""
Serializers for Watcher
"""

from rest_framework import serializers
from core.models import Watcher

class WatcherSerializer(serializers.ModelSerializer):
    """Serializer for Watcher"""

    class Meta:
        model = Watcher
        fields = ['id', 'issue', 'watcher', 'is_active', 'created_at', 'updated_at']
        read_only_fields = ['id',]