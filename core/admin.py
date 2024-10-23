from django.contrib import admin
from .models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_language', 'target_language', 'status', 'uploaded_by', 'created_at')
    list_filter = ('status', 'source_language', 'target_language', 'created_at')
    search_fields = ('title', 'uploaded_by__username')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ('original_file',)
        return self.readonly_fields
