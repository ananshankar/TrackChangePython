"""
Serializers for Comments app
"""

from rest_framework import serializers
from core.models import IssueComments

class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment"""

    class Meta:
        model = IssueComments
        fields = ['id', 'comment', 'issue', 'user', 'created_at', 'updated_at']
        read_only_fields = ['id',]