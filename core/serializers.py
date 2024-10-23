from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name')

class DocumentSerializer(serializers.ModelSerializer):
    uploaded_by = UserSerializer(read_only=True)
    
    class Meta:
        model = Document
        fields = '__all__'
        read_only_fields = ('uploaded_by', 'created_at', 'updated_at', 'status')

class DocumentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('title', 'original_file', 'source_language', 'target_language')

