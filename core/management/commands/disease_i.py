from django.core.management.base import BaseCommand, CommandError
from HPS.main import disease_mapping
from core.models import DESEASE
from termcolor import colored  # for colorful terminal messages
class Command(BaseCommand):
    help = "Inserting desease"


    def handle(self, *args, **options):
        
        self.stdout.write(colored("inserting diseases...","green"))
        self.stdout.write(colored("deleting diseases...","red"))
        DESEASE.objects.all().delete()
        
        
        for value in disease_mapping.values():
            
            DESEASE.objects.create(name=value)
        
        
        self.stdout.write(colored("all diseases enter successfully.","green"))