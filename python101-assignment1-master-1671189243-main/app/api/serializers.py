from django.contrib.auth.models import User as User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"

    def create(self, validated_data):
        user = User.objects.create_user(username=validated_data['username'],email=validated_data['email'])
        user.set_password(validated_data['password'])
        user.save()
        return user