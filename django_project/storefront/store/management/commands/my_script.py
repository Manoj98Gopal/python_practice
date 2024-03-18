# my_script.py
import os
import json
from django.core.management.base import BaseCommand
from store.models import Customer

class Command(BaseCommand):
    help = 'Description of your command here'

    
    def handle(self, *args, **options):
        json_file_path = os.path.join(os.getcwd(), 'dummy_data.json')
        with open(json_file_path, 'r') as file:
            data = json.load(file)
            
            for obj in data:
                Customer.objects.create(
                    first_name=obj['first_name'],
                    last_name=obj['last_name'],
                    email=obj['email'],
                    phone=obj['phone'],
                    birth_date=obj['birth_date'],
                    membership=obj['membership']
                )
            
            print("sussfully created....")    
            
            self.stdout.write(self.style.SUCCESS('Data added successfully'))
    
        # Your script logic here
        