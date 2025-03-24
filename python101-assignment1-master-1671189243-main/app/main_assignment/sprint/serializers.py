# """
# Serializers for the Sprint app
# """

from rest_framework import serializers
from core.models import Sprint

class SprintSerializer(serializers.ModelSerializer):
    """Serializer for Sprint"""

    class Meta:
        model = Sprint
        fields = [
            'id', 'project', 'label', 'start_date',
            'end_date', 'created_at', 'updated_at',
        ]
        read_only_fields = ['id',]