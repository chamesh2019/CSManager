from rest_framework import serializers
from .models import Module, Document

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = '__all__' 

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'