from rest_framework import serializers
from ..models import Subject, Module, Content


class SubjectSerializer(serializers.ModelSerializer):
     class Meta:
          model = Subject
          fields = ['id', 'title', 'slug']