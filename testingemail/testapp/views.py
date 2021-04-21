from django.shortcuts import render
from .models import TestingEmails
from .serializers import TestingSerializer
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import permissions
from .mail import send_welcome_mail

@permission_classes((permissions.AllowAny,))
class EmailTestingViews(viewsets.ModelViewSet):
    serializer_class = TestingSerializer
    queryset = TestingEmails.objects.all()

    def post(self, request):
        print('dd',request.data)
        serializer = TestingSerializer(data=request.data)
        print('ser', serializer)
        if serializer.is_valid():
            serializer.save()
            send_welcome_mail(test_object)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@permission_classes((permissions.AllowAny,))
class TestEmailViews(viewsets.ViewSet):
    serializer_class = TestingSerializer
    queryset = TestingEmails.objects.all()
    # def list(self, request):
    #     queryset = TestingEmails.objects.all()
    #     serializer = TestingSerializer(queryset, many=True)
    #     return Response(serializer.data)

    def create(self, request):
        test_object = TestingEmails()
        test_object.email = request.data.get('email')
        test_object.files = request.data.get('file')
        test_object.save()
        send_welcome_mail(test_object)
        return Response({'response': 'saves'})
