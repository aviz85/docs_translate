from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from core.models import Document
from faker import Faker
from django.core.files import File
from django.conf import settings
import random
import os

class Command(BaseCommand):
    help = 'Generates fake data for testing'

    def handle(self, *args, **kwargs):
        fake = Faker()
        
        # Create sample users if they don't exist
        if User.objects.count() == 0:
            # Create superuser
            User.objects.create_superuser(
                username='admin',
                email='admin@example.com',
                password='admin123'
            )
            
            # Create regular users
            for _ in range(5):
                User.objects.create_user(
                    username=fake.user_name(),
                    email=fake.email(),
                    password='password123',
                    first_name=fake.first_name(),
                    last_name=fake.last_name()
                )
        
        users = User.objects.all()
        
        # Languages for testing
        languages = ['en', 'he', 'fr', 'es', 'de', 'ru']
        statuses = ['pending', 'in_progress', 'completed', 'failed']
        
        # Create sample documents
        for _ in range(20):
            source_lang = random.choice(languages)
            target_lang = random.choice([l for l in languages if l != source_lang])
            
            # Create a dummy file for testing
            dummy_file_path = os.path.join(settings.MEDIA_ROOT, 'documents/original/dummy.docx')
            os.makedirs(os.path.dirname(dummy_file_path), exist_ok=True)
            
            # Create an empty file if it doesn't exist
            if not os.path.exists(dummy_file_path):
                with open(dummy_file_path, 'w') as f:
                    f.write('dummy content')
            
            document = Document.objects.create(
                title=fake.catch_phrase(),
                source_language=source_lang,
                target_language=target_lang,
                uploaded_by=random.choice(users),
                status=random.choice(statuses)
            )
            
            # Add dummy file
            with open(dummy_file_path, 'rb') as file:
                document.original_file.save(
                    f'document_{document.id}.docx',
                    File(file),
                    save=True
                )
            
            self.stdout.write(f'Created document: {document.title}')
        
        self.stdout.write(self.style.SUCCESS('Successfully generated fake data'))