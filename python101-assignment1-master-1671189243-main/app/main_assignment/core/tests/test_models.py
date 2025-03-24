"""Tests for models"""

from core import models
from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):
    """Test models"""

    def test_create_user(self):
        """Test creating a new user"""
        email = "test@example.com"
        password = "test_password"
        username = "test_username"
        user = get_user_model().objects.create_user(
            email=email,
            password=password,
            username=username
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_without_email_raises_error(self,):
        """Creating a new user without an email raises an error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test_username", "test_password")

    def test_create_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            "test@example.com",
            "test_superuser",
            "test_password"
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
    
    def test_create_project(self):
        """Test creating a new project"""
        user = get_user_model().objects.create_user(
            "test@example.com",
            "test_username",
            "test_password"
        )
        name = "Test Project"
        start_date = "2022-09-08 09:10:10"
        project = models.Project.objects.create(
            user=user,
            project_name=name,
            start_date=start_date
        )

        self.assertEqual(project.project_name, name)

    # def test_create_sprint(self):
    #     """Test creating a new sprint"""
    #     project = models.Project.objects.create(
    #         project_name="Test Project",
    #         start_date="2022-09-08 09:10:10"
    #     )
    #     name = "Test Sprint"
    #     sprint = models.Sprint.objects.create(
    #         project=project,
    #         sprint_name=name
    #     )

    #     self.assertEqual(sprint.sprint_name, name)
    #     self.assertEqual(sprint.project, project)
    
    # def test_create_issue(self):
    #     """Test creating a new issue"""
    #     project = models.Project.objects.create(
    #         project_name="Test Project",
    #         start_date="2022-09-08 09:10:10"
    #     )
    #     sprint = models.Sprint.objects.create(
    #         project=project,
    #         sprint_name="Test Sprint"
    #     )
    #     name = "Test Issue"
    #     issue = models.Issue.objects.create(
    #         sprint=sprint,
    #         title=name
    #     )

    #     self.assertEqual(issue.title, name)
    #     self.assertEqual(issue.sprint, sprint)