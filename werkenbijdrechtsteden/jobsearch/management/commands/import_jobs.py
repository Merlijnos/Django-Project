# jobsearch/management/commands/import_jobs.py
import json
from django.core.management.base import BaseCommand
from jobsearch.models import JobListing

class Command(BaseCommand):
    help = 'Import job listings from a JSON file'

    def handle(self, *args, **options):
        with open('jobsearch/fixtures/mock_data.json', 'r') as f:
            jobs_json = json.load(f)

        for job_data in jobs_json:
            JobListing.objects.create(**job_data)

        self.stdout.write(self.style.SUCCESS('Successfully imported job listings'))