"""
Views for the Project APIs
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from core.models import Project
from project import serializers

class ProjectViewSet(viewsets.ModelViewSet):
    """View for manage Project APIs"""

    serializer_class = serializers.ProjectSerializer
    queryset = Project.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve projects for the authenticated user"""

        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    def get_serializer_class(self):
        """Return serializer class for request"""

        if self.action == 'list':
            return serializers.ProjectSerializer
        return self.serializer_class
    
    def perform_create(self, serializer):
        """Create a new Project"""

        serializer.save(user=self.request.user)
    
    def destroy(self, request, *args, **kwargs):
        """Delete a project"""

        project = self.get_object()
        project.delete()
        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )

# class SprintViewSet(mixins.DestroyModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.ListModelMixin,
#                     viewsets.GenericViewSet):
#     """View for manage Sprint APIs"""

#     serializer_class = serializers.SprintSerializer
#     queryset = Sprint.objects.all()
#     authentication_classes = [TokenAuthentication]
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         """Retrieve sprints for the authenticated user"""

#         return self.queryset.filter(project__user=self.request.user).order_by('-id')
    
#     def create(self, serializer):
#         """Create a new sprint"""

#         serializer.save(project__user=self.request.user)
    
#     def destroy(self, request, *args, **kwargs):
#         """Delete a sprint"""

#         sprint = self.get_object()
#         sprint.delete()
#         return Response(
#             {"success" : "yes"},
#             status=status.HTTP_200_OK
#         )