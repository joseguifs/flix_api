from django.core.management.base import BaseCommand
from actors.models import Actors
import csv 


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument(
            'file_name',
            type=str,
            help='file_name = nome do arquivo'
        )
    
    
    def handle(self, *args, **options):
        file_name = options['file_name']

        with open(file_name, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for raw in reader:  
                name = raw['name']
                nationality = raw['nationality']

                self.stdout.write(self.style.NOTICE(name))
            
                Actors.objects.create(
                    name = name,
                    nationality = nationality
                )
            
            self.stdout.write(self.style.SUCCESS('Atores importados com sucesso !'))