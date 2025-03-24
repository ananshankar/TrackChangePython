"""
Serializers for the Project app
"""

from rest_framework import serializers
from core.models import Project, Sprint, Issue

class ProjectSerializer(serializers.ModelSerializer):
    """Serializer for Project"""

    class Meta:
        model = Project
        fields = ['id', 'project_name', 'start_date', 'created_at', 'updated_at']
        read_only_fields = ['id',]

class ProjectDetailSerializer(ProjectSerializer):
    """Serializer for Project Detail"""

    class Meta(ProjectSerializer.Meta):
        fields = ProjectSerializer.Meta.fields + ['user']