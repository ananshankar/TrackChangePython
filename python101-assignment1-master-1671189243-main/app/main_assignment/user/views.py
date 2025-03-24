"""
Views for the User API
"""

from core.models import User, Project, UserProjectRelation
from django.contrib.auth import get_user_model
from rest_framework import generics, authentication, permissions, status, viewsets, mixins
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from rest_framework.response import Response
from user.serializers import (
    UserSerializer,
    UserDetailSerializer,
    AuthTokenSerializer,
    UserProjectRelationSerializer
)

class CreateUserView(generics.CreateAPIView):
    """Create a new user in the system"""
    serializer_class = UserSerializer

    def login(self, request, *args, **kwargs):
        """Create a new user"""

        User = get_user_model()
        email = request.data.get('email')
        if User.objects.filter(email=email).exists():
            user = User.objects.get(email=email)
            serializer = self.get_serializer(user)
            return Response(
                {
                    'status' : 'success',
                    'code' : '200',
                },
                status=status.HTTP_200_OK
            )

        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {'data' : serializer.data},
            status=status.HTTP_201_CREATED
        )

class CreateTokenView(ObtainAuthToken):
    """Create a new auth token for user"""
    serializer_class = AuthTokenSerializer
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES

class ManageUserView(generics.RetrieveUpdateAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user

class UserViewSet(viewsets.ModelViewSet):
    """View for manage User APIs"""

    serializer_class = UserDetailSerializer
    queryset = User.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve users"""

        return self.queryset.all()
    
    def destroy(self, request, *args, **kwargs):
        """Delete a user"""

        user = self.get_object()
        user.delete()
        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )
    
class UserProjectRelationViewset(mixins.DestroyModelMixin,
                                 mixins.UpdateModelMixin,
                                 mixins.ListModelMixin,
                                 viewsets.GenericViewSet):
    """View for manage UserProjectRelation APIs"""

    serializer_class = UserProjectRelationSerializer
    queryset = UserProjectRelation.objects.all()
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """Retrieve projects for the authenticated user"""

        project_id = self.request.query_params.get('project')
        if project_id:
            return self.queryset.filter(project=project_id)

        return self.queryset
    
    def create(self, request, *args, **kwargs):
        """Assign users to a project"""
        project_id = request.data.get('project')
        user_ids = request.data.get('user')

        if not project_id or not user_ids:
            return Response(
                {"success":"False"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response(
                {"error": "No valid project found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        users = get_user_model().objects.filter(id__in=user_ids)
        if not users.exists():
            return Response(
                {"error": "No valid users or project found"},
                status=status.HTTP_400_BAD_REQUEST
            )

        for user in users:
            project_relation = UserProjectRelation.objects.create(
                user=user,
                project=project
            )
            project_relation.save()

        return Response(
            {
                "success" : "True",
                "data" : UserProjectRelationSerializer(project_relation).data
            },
            status=status.HTTP_200_OK
        )

    def update(self, request, *args, **kwargs):
        """Update a project relation"""
        
        is_active = request.data.get('is_active')
        project_relation = self.get_object()
        project_relation.is_active = is_active
        project_relation.save()

        return Response(
            UserProjectRelationSerializer(project_relation).data,
            status=status.HTTP_200_OK
        )

    def destroy(self, request, *args, **kwargs):
        """Delete a project relation"""

        project_relation = self.get_object()
        project_relation.delete()
        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )