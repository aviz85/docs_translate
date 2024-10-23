from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Document
from .forms import DocumentForm
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .serializers import DocumentSerializer, DocumentCreateSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .permissions import IsOwner

# Create your views here.

def home(request):
    return render(request, 'core/home.html')

@login_required
def document_list(request):
    documents = Document.objects.filter(uploaded_by=request.user)
    return render(request, 'core/document_list.html', {'documents': documents})

@login_required
def upload_document(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            document = form.save(commit=False)
            document.uploaded_by = request.user
            document.save()
            messages.success(request, 'Document uploaded successfully!')
            return redirect('document_list')
    else:
        form = DocumentForm()
    return render(request, 'core/upload_document.html', {'form': form})

class DocumentViewSet(viewsets.ModelViewSet):
    """
    ViewSet for managing documents.
    """
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = DocumentSerializer
    
    def get_queryset(self):
        return Document.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @swagger_auto_schema(
        operation_description="List all documents for the current user",
        responses={200: DocumentSerializer(many=True)}
    )
    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Create a new document",
        request_body=DocumentCreateSerializer,
        responses={
            201: DocumentSerializer,
            400: "Bad Request",
            401: "Unauthorized"
        }
    )
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_description="Get a specific document by ID",
        responses={
            200: DocumentSerializer,
            404: "Not Found"
        }
    )
    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)

    @swagger_auto_schema(
        method='post',
        operation_description="Start translation process for a document",
        responses={
            200: openapi.Response(
                description="Translation started",
                examples={
                    "application/json": {
                        "status": "translation started"
                    }
                }
            ),
            404: "Document not found",
            400: "Translation error"
        }
    )
    @action(detail=True, methods=['post'])
    def translate(self, request, pk=None):
        """
        Trigger translation for a specific document.
        """
        document = self.get_object()
        document.status = 'in_progress'
        document.save()
        return Response({'status': 'translation started'})
