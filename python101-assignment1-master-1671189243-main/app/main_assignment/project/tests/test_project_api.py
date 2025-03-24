"""
Tests for Project API
"""

import pytz
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from core.models import Project
from django.utils.dateparse import parse_datetime
from project.serializers import ProjectSerializer, ProjectDetailSerializer

PROJECT_URL = reverse('project:project-list')

def detail_url(project_id):
    """Create and return project detail URL"""

    return reverse('project:project-detail', args=[project_id])

def create_project(user, **params):
    """Create and return a sample project"""

    defaults = {
        'project_name' : 'Test Project',
        'start_date' : '2022-09-08 09:10:10',
        'created_at' : '2022-09-08 09:10:10',
        'updated_at' : '2022-09-08 09:10:10'
    }
    defaults.update(params)

    project = Project.objects.create(user=user, **defaults)
    return project

def create_user(**params):
    """Create and return a user"""

    return get_user_model().objects.create_user(**params)

class PublicProjectApiTests(TestCase):
    """Test unauthenticated API requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API"""
        res = self.client.get(PROJECT_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

class PrivateProjectApiTests(TestCase):
    """Test authenticated API requests"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com',username='test_user_2',password='testpass')
        self.client.force_authenticate(self.user)

    def test_retrieve_all_projects(self):
        """Test retrieving a list of projects"""

        create_project(user=self.user)
        create_project(user=self.user)

        response = self.client.get(PROJECT_URL)

        projects = Project.objects.all().order_by('-id')
        serializer = ProjectSerializer(projects, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
    
    def test_retrieve_project_by_id(self):
        """Test retrieving a project by id"""

        project = create_project(user=self.user)

        response = self.client.get(reverse('project:project-detail', args=[project.id]))

        serializer = ProjectSerializer(project)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['project_name'], serializer.data['project_name'])

    def test_project_detail(self):
        """Test get project detail"""

        project = create_project(user=self.user)

        url = detail_url(project.id)
        response = self.client.get(url)

        serializer = ProjectDetailSerializer(project)
        self.assertEqual(response.data['project_name'], serializer.data['project_name'])
    
    def test_create_project(self):
        """Test creating a new project"""

        payload = {
            'user' : 10,
            'project_name' : 'Test Project',
            'start_date' : '2022-09-08 09:10:10',
            'created_at' : '2022-09-08 09:10:10',
            'updated_at' : '2022-09-08 09:10:10'
        }

        response = self.client.post(PROJECT_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        project = Project.objects.get(id=response.data['id'])
        self.assertEqual(project.user, self.user)
    
    def test_partial_update(self):
        """Test partial update of a project"""

        project = create_project(user=self.user)

        payload = {'project_name' : 'New Project Name'}
        url = detail_url(project.id)
        response = self.client.patch(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        project.refresh_from_db()
        self.assertEqual(project.project_name, payload['project_name'])
        self.assertEqual(project.user, self.user)
    
    def test_full_update(self):
        """Test full update of a project"""

        project = create_project(user=self.user)

        payload = {
            'user' : self.user.id,
            'project_name' : 'New Project Name',
            'start_date' : '2024-09-08 09:10:10',
            'created_at' : '2024-09-08 09:10:10',
            'updated_at' : '2024-09-08 09:10:10'
        }
        url = detail_url(project.id)
        response = self.client.put(url, payload)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        project.refresh_from_db()
        self.assertEqual(project.user, self.user)
        self.assertEqual(project.project_name, payload['project_name'])
    
    def test_update_user_returns_error(self):
        """Test updating user field returns error"""

        project = create_project(user=self.user)
        new_user = create_user(email='user10@example.com',username='test_user_10',password='testpass')

        payload = {'user' : new_user.id}
        url = detail_url(project.id)

        self.client.put(url, payload)

        project.refresh_from_db()
        self.assertEqual(project.user, self.user)
    
    def test_delete_project(self):
        """Test deleting a project"""

        project = create_project(user=self.user)

        url = detail_url(project.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Project.objects.filter(id=project.id).exists())
    
    def test_project_other_users_project_error(self):
        """Test trying to delete other users project returns error"""

        new_user = create_user(email='user20@example.com',username='test_user_20',password='testpass')
        project = create_project(user=new_user)

        url = detail_url(project.id)
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertTrue(Project.objects.filter(id=project.id).exists())