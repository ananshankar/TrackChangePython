"""
Tests for Sprint API
"""

from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Sprint, Project
from sprint.serializers import SprintSerializer

SPRINT_URL = reverse('sprint:sprint-list')

def create_sprint(project, **params):
    """Create and return a sample sprint"""

    defaults = {
        'sprint_name' : 'Test Sprint',
        'start_date' : '2022-09-08 09:10:10',
        'end_date' : '2022-09-08 09:10:10',
        'created_at' : '2022-09-08 09:10:10',
        'updated_at' : '2022-09-08 09:10:10'
    }
    defaults.update(params)

    sprint = Sprint.objects.create(project=project, **defaults)
    return sprint

class PublicSprintApiTests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(SPRINT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

# class PrivateSprintApiTests(TestCase):
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
    
#     def test_retrieve_all_sprints(self):
#         """Test retrieving a list of sprints"""

#         create_sprint(project=self.project)
#         create_sprint(project=self.project)

#         response = self.client.get(SPRINT_URL)

#         sprints = Sprint.objects.all().order_by('-id')
#         serializer = SprintSerializer(sprints, many=True)

#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['sprint_name'], serializer.data['sprint_name'])