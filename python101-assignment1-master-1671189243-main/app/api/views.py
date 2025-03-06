from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import viewsets, status
from rest_framework.authtoken.models import Token
from rest_framework.status import HTTP_200_OK
from rest_framework.views import APIView
from django.contrib.auth.models import User as User
from .serializers import UserSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
import logging
logger = logging.getLogger(__name__)


import subprocess
from pathlib import Path

class CarsView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_test_cases_result(self, request):
        test_file_path = Path(__file__).resolve().parent.parent / "assignment1" / "tests" / "test_cars.py"
        cmd = ["pytest", "-v", str(test_file_path)]
        test_case_output = subprocess.run(cmd, capture_output=True)

        lines = test_case_output.stdout.decode().split("\n")
        results = {}
        for line in lines:
            if "TestCars" in line and "PASSED" in line or "FAILED" in line:
                test_case_result = line.split(" ")
                if test_case_result[0] != "FAILED":
                    test_case, result = test_case_result[0].split("::")[-1], test_case_result[1]
                    results[test_case] = result

        return Response(results, status=status.HTTP_200_OK)


class StatesView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_test_cases_result(self, request):
        test_file_path = Path(__file__).resolve().parent.parent / "assignment1" / "tests" / "test_states.py"
        cmd = ["pytest", "-v", str(test_file_path)]
        test_case_output = subprocess.run(cmd, capture_output=True)
        lines = test_case_output.stdout.decode().split("\n")
        results = {}
        for line in lines:
            if "TestStates" in line and "PASSED" in line or "FAILED" in line:
                test_case_result = line.split(" ")
                if test_case_result[0] != "FAILED":
                    test_case, result = test_case_result[0].split("::")[-1], test_case_result[1]
                    results[test_case] = result

        return Response(results, status=status.HTTP_200_OK)

class FriendsView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_test_cases_result(self, request):
        test_file_path = Path(__file__).resolve().parent.parent / "assignment1" / "tests" /"test_friends.py"
        cmd = ["pytest", "-v", str(test_file_path)]
        test_case_output = subprocess.run(cmd, capture_output=True)

        lines = test_case_output.stdout.decode().split("\n")
        results = {}
        for line in lines:
            if "TestFriends" in line and "PASSED" in line or "FAILED" in line:
                test_case_result = line.split(" ")
                if test_case_result[0] != "FAILED":
                    test_case, result = test_case_result[0].split("::")[-1], test_case_result[1]
                    results[test_case] = result

        return Response(results, status=status.HTTP_200_OK)

class ProfileView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_test_cases_result(self, request):
        test_file_path = Path(__file__).resolve().parent.parent / "assignment2" / "tests" / "test_get_profile.py"
        cmd = ["pytest", "-v", str(test_file_path)]
        test_case_output = subprocess.run(cmd, capture_output=True)

        lines = test_case_output.stdout.decode().split("\n")
        results = {}
        for line in lines:
            if "TestProfile" in line and "PASSED" in line or "FAILED" in line:
                test_case_result = line.split(" ")
                if test_case_result[0] != "FAILED":
                    test_case, result = test_case_result[0].split("::")[-1], test_case_result[1]
                    results[test_case] = result

        return Response(results, status=status.HTTP_200_OK)

class DataStructuresView(viewsets.ViewSet):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    @action(detail=True, methods=['get'])
    def get_test_cases_result(self, request):
        test_file_path = Path(__file__).resolve().parent.parent / "assignment1" / "tests" / "test_data_structures.py"
        cmd = ["pytest", "-v", str(test_file_path)]
        test_case_output = subprocess.run(cmd, capture_output=True)

        lines = test_case_output.stdout.decode().split("\n")
        results = {}
        for line in lines:
            if "TestDataStructures" in line and "PASSED" in line or "FAILED" in line:
                test_case_result = line.split(" ")
                if test_case_result[0] != "FAILED":
                    test_case, result = test_case_result[0].split("::")[-1], test_case_result[1]
                    results[test_case] = result

        return Response(results, status=status.HTTP_200_OK)

class UserView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):

        try:
            if id is not None:
                user = User.objects.filter(id=id).first()
                if user is None:
                    return Response({"error":"User with this id doesn't exist"})
                response = UserSerializer(user)
                return Response(response.data)
        except Exception as e:
            logger.info(f"Exception while fetching user", e)

        users = User.objects.all()
        response = UserSerializer(users, many=True)
        return Response(response.data)


class TokenView(APIView):

    def post(self, request, *args, **kwargs):
        data = request.data
        user = User.objects.filter(username=data['username']).first()
        if user is None:
            serializer = UserSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            logger.info('user created')
            user = User.objects.get(username=serializer.data['username'])
            token_obj, _ = Token.objects.get_or_create(user=user)

            return Response({'token': str(token_obj), 'data': serializer.data}, status=201)

        if not user.check_password(data.get("password")):
            return Response({"password": ["Wrong password."]}, status=status.HTTP_400_BAD_REQUEST)
        token_obj = Token.objects.get(user=user)
        if token_obj is None:
            return Response({"error": "Token for this user doesn't exist"})
        response = {
            'status': 'success',
            'code': status.HTTP_200_OK,
            'token': str(token_obj),
        }

        return Response(response, status=HTTP_200_OK)






