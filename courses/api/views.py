from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from django.shortcuts import get_object_or_404

from .serializers import SubjectSerializer
from ..models import Subject, Course, Module


class SubjectListView(generics.ListAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class SubjectDetailView(generics.RetrieveAPIView):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer


class CourseEnrollView(APIView):
    authentication_classes = (BasicAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, pk, formt=None):
        course = get_object_or_404(Course, pk=pk)
        course.students.add(request.user)

        return Response({
            'data': {
                'enrolled': True
            }
        })
