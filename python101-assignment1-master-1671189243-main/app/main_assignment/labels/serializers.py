from rest_framework import serializers
from core.models import Labels

class LabelSerializer(serializers.ModelSerializer):
    """Serializer for Labels"""

    class Meta:
        model = Labels
        fields = ['id', 'label', 'issue', 'created_at', 'updated_at']
        read_only_fields = ['id',]