"""
Views for Comments app
"""

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import IssueComments
from issue_comments import serializers

class CommentViewSet(viewsets.ModelViewSet):
    """View for manage Comment APIs"""

    serializer_class = serializers.CommentSerializer
    queryset = IssueComments.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve comments for the authenticated user"""

        return self.queryset.filter(issue__sprint__project__user=self.request.user).order_by('-id')
    
    def destroy(self, request, *args, **kwargs):
        """Delete a comment"""

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )