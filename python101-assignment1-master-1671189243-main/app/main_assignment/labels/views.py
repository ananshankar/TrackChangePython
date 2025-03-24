"""
Views for the Labels APIs
"""

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Labels
from labels import serializers

class LabelViewSet(viewsets.ModelViewSet):
    """View for manage Watcher APIs"""

    serializer_class = serializers.LabelSerializer
    queryset = Labels.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve labels for the authenticated user"""

        return self.queryset.filter(issue__sprint__project__user=self.request.user).order_by('-id')
    
    def destroy(self, request, *args, **kwargs):
        """Delete a label"""

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )