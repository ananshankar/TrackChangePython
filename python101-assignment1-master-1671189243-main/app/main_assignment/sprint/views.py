"""
Views for the Sprint APIs
"""

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from core.models import Sprint, Project
from rest_framework.response import Response
from sprint import serializers

class SprintViewSet(viewsets.ModelViewSet):
    """View for manage Sprint APIs"""

    serializer_class = serializers.SprintSerializer
    queryset = Sprint.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve sprints for the authenticated user"""

        return self.queryset.filter(project__user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new sprint"""

        project_id = self.request.data.get('project')

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response(
                {"error": "Project not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer.save(project=project)

    def destroy(self, request, *args, **kwargs):
        """Delete a sprint"""

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )