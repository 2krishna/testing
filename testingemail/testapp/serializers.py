from rest_framework import serializers
from .models import TestingEmails

class TestingSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestingEmails
        fields = ['email', 'files']
