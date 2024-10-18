# save_data_to_s3.py
import boto3
import json
from django.core.management.base import BaseCommand
from django.core.files.base import ContentFile
from .models import City
from storages.backends.s3boto3 import S3Boto3Storage


class Command(BaseCommand):
    help = 'Save data to S3 as JSON'
    @staticmethod
    def handle( *args, **options):
        # Fetch data from your Django model
        data = City.objects.all().values()

        # Convert data to JSON
        json_data = json.dumps(list(data), indent=2)

        # Save JSON data to S3
        storage = S3Boto3Storage()
        file_name = 'data.json'
        file_content = ContentFile(json_data.encode())
        storage.save(file_name, file_content)
        print("Success")


        # self.stdout.write(self.style.SUCCESS('Data saved to S3 successfully'))
