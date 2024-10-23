from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Document

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class DocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ('id', 'title', 'source_language', 'target_language', 
                 'original_file', 'translated_file', 'status', 'created_at')
        read_only_fields = ('status', 'translated_file')

class DocumentCreateSerializer(serializers.ModelSerializer):
    """
    Serializer for creating new Document instances.
    """
    class Meta:
        model = Document
        fields = ('title', 'original_file', 'source_language', 'target_language')
        extra_kwargs = {
            'title': {'help_text': 'The title of the document'},
            'original_file': {'help_text': 'The document file to be translated'},
            'source_language': {'help_text': 'The language code of the original document'},
            'target_language': {'help_text': 'The language code for translation'},
        }
