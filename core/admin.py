from django.contrib import admin
from .models import Document

# Register your models here.

@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'source_language', 'target_language', 'status', 'created_at')
    list_filter = ('status', 'source_language', 'target_language')
    search_fields = ('title', 'user__username')
    readonly_fields = ('created_at', 'updated_at')
    
    def get_queryset(self, request):
        return super().get_queryset(request).select_related('user')
