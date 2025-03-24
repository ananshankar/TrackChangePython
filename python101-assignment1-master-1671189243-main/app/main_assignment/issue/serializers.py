"""
Serializers for the Issue app
"""

from rest_framework import serializers
from core.models import Issue

class IssueSerializer(serializers.ModelSerializer):
    """Serializer for Issue"""

    class Meta:
        model = Issue
        fields = [
            'id', 'sprint', 'title', 'issue_type',
            'issue_status', 'created_at', 'updated_at',
            'assignee'
        ]
        read_only_fields = ['id',]