"""
Tests for Issue API
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Issue, Sprint, Project
from issue.serializers import IssueSerializer

ISSUE_URL = reverse('issue:issue-list')

def create_issue(sprint, **params):
    """Create and return a sample issue"""

    defaults = {
        'title' : 'Test Issue',
        'issue_type' : 'Task',
        'issue_status' : 'Open',
        'created_at' : '2022-09-08 09:10:10',
        'updated_at' : '2022-09-08 09:10:10'
    }
    defaults.update(params)

    issue = Issue.objects.create(sprint=sprint, **defaults)
    return issue

class PublicIssueApiTests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(ISSUE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

# class PrivateIssueApiTests(TestCase):
#     """Test authenticated API requests"""

#     def setUp(self):
#         self.client = APIClient()
#         self.user = get_user_model().objects.create_user(
#             'user@example.com',
#             'test_username',
#             'test_password'
#         )
#         self.client.force_authenticate(self.user)
#         self.project = Project.objects.create(
#             user=self.user,
#             project_name='Test Project',
#             start_date='2022-09-08 09:10:10',
#             created_at='2022-09-08 09:10:10',
#             updated_at='2022-09-08 09:10:10'
#         )
#         self.sprint = Sprint.objects.create(
#             project=self.project,
#             sprint_name='Test Sprint',
#             start_date='2022-09-08 09:10:10',
#             end_date='2022-09-08 09:10:10',
#             created_at='2022-09-08 09:10:10',
#             updated_at='2022-09-08 09:10:10'
#         )

#     def test_retrieve_all_issues(self):
#         """Test retrieving a list of issues"""

#         create_issue(sprint=self.sprint)
#         create_issue(sprint=self.sprint)

#         response = self.client.get(ISSUE_URL)

#         issues = Issue.objects.all().order_by('-id')
#         serializer = IssueSerializer(issues, many=True)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['title'], serializer.data['title'])