"""
Views for the Watcher APIs
"""

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from core.models import Watcher
from watcher import serializers

class WatcherViewSet(viewsets.ModelViewSet):
    """View for manage Watcher APIs"""

    serializer_class = serializers.WatcherSerializer
    queryset = Watcher.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve watchers for the authenticated user"""

        return self.queryset.filter(issue__sprint__project__user=self.request.user).order_by('-id')
    
    def destroy(self, request, *args, **kwargs):
        """Delete a watcher"""

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['put'], url_name='update-status')
    def update_status(self, request, *args, **kwargs):
        """Update a watcher"""

        user = self.request.query_params.get('user')
        issue = self.request.query_params.get('issue')

        if not user or not issue:
            return Response(
                {"error": "User and Issue required"},
                status=status.HTTP_404_NOT_FOUND
            )

        try:
            instance = self.queryset.get(watcher=user, issue=issue)
        except Watcher.DoesNotExist:
            return Response(
                {"error": "Watcher not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        instance.is_active = False
        instance.save()

        return Response(
            serializers.WatcherSerializer(instance).data,
            status=status.HTTP_200_OK
        )