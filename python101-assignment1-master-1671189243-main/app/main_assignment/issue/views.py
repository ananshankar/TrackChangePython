"""
Views for the Issue APIs
"""

from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import action
from django.db.models import Q
from core.models import Issue, Sprint, Project
from issue import serializers

class IssueViewSet(viewsets.ModelViewSet):
    """View for manage Issue APIs"""

    serializer_class = serializers.IssueSerializer
    queryset = Issue.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve issues for the authenticated user"""

        return self.queryset.filter(sprint__project__user=self.request.user).order_by('-id')

    def perform_create(self, serializer):
        """Create a new issue"""

        sprint_id = self.request.data.get('sprint')

        try:
            sprint = Sprint.objects.get(id=sprint_id)
        except Sprint.DoesNotExist:
            return Response(
                {"error": "Sprint not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer.save(sprint=sprint)

    def destroy(self, request, *args, **kwargs):
        """Delete a issue"""

        instance = self.get_object()
        self.perform_destroy(instance)

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['put'])
    def sprints(self, request, *args, **kwargs):
        """Move issue to another sprint"""

        sprint_id = request.data.get('sprint')
        issues = request.data.get('issues')
        if not sprint_id or not issues:
            return Response(
                {"message":"sprint and issues are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            sprint = Sprint.objects.get(id=sprint_id)
        except Sprint.DoesNotExist:
            return Response(
                {"error": "Sprint not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        for issue in issues:
            try:
                issue = Issue.objects.get(id=issue)
                issue.sprint = sprint
                issue.save()
            except Issue.DoesNotExist:
                return Response(
                    {"error": "Issue not found"},
                    status=status.HTTP_404_NOT_FOUND
                )

        return Response(
            {"success" : "yes"},
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'], url_path='by-project')
    def get_issues_by_project(self, request, *args, **kwargs):
        """Get all issues of a project by project ID"""

        project_id = request.query_params.get('project_id')
        if not project_id:
            return Response(
                {"error": "project_id is required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            project = Project.objects.get(id=project_id)
        except Project.DoesNotExist:
            return Response(
                {"error": "Project not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        issues = self.queryset.filter(sprint__project=project).order_by('-updated_at')
        page = self.paginate_queryset(issues)
        if page is not None:
            return self.get_paginated_response(serializers.IssueSerializer(page, many=True).data)

        return Response(
            serializers.IssueSerializer(issues, many=True).data,
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['put'], url_path='update-status')
    def update_issue_status(self, request, *args, **kwargs):
        """Update status of an issue"""

        issue = self.request.query_params.get('issue')
        new_status = self.request.query_params.get('status')
        if not issue or not status:
            return Response(
                {"error": "issue and status are required"},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        try:
            instance = Issue.objects.get(id=issue)
        except Issue.DoesNotExist:
            return Response(
                {"error": "Issue not found"},
                status=status.HTTP_404_NOT_FOUND
            )
        
        instance.issue_status = new_status
        instance.save()

        return Response(
            serializers.IssueSerializer(instance).data,
            status=status.HTTP_200_OK
        )
    
    @action(detail=False, methods=['get'], url_path='search')
    def search_issues(self, request, *args, **kwargs):
        """Search issues by parameters"""

        project = self.request.query_params.get('project')
        title = self.request.query_params.get('title')
        issue_type = self.request.query_params.get('type')
        issue_status = self.request.query_params.get('status')
        assignee = self.request.query_params.get('assignee')
        label = self.request.query_params.get('label')
        condition = self.request.query_params.get('condition', 'AND').upper()

        query = Q()
        if condition == 'AND':
            if project:
                query &= Q(sprint__project__id=project)
            if title:
                query &= Q(title__icontains=title)
            if issue_type:
                query &= Q(issue_type=issue_type)
            if issue_status:
                query &= Q(issue_status=issue_status)
            if assignee:
                query &= Q(assignee__id=assignee)
            if label:
                query &= Q(label__icontains=label)
        else:
            or_query = Q()
            if project:
                or_query |= Q(sprint__project__id=project)
            if title:
                or_query |= Q(title__icontains=title)
            if issue_type:
                or_query |= Q(issue_type=issue_type)
            if issue_status:
                or_query |= Q(issue_status=issue_status)
            if assignee:
                or_query |= Q(assignee__id=assignee)
            if label:
                or_query |= Q(label__icontains=label)
            query = or_query

        issues = self.queryset.filter(query).order_by('-updated_at')
        page = self.paginate_queryset(issues)
        if page is not None:
            return self.get_paginated_response(serializers.IssueSerializer(page, many=True).data)

        return Response(
            serializers.IssueSerializer(issues, many=True).data,
            status=status.HTTP_200_OK
        )