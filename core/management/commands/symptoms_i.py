from django.core.management.base import BaseCommand, CommandError
from HPS.main import all_symptoms
from core.models import SYMPTOMS
from termcolor import colored  # for colorful terminal messages



class Command(BaseCommand):
    help = "Inserting symptoms"
    
    def handle(self, *args, **options):
        
        self.stdout.write(colored("inserting symptoms...","green"))
        self.stdout.write(colored("deletting symptoms...","red"))
        
        SYMPTOMS.objects.all().delete()
        
        self.stdout.write(colored("symptoms deleted.","yellow"))
        
        for value in all_symptoms:
            
            SYMPTOMS.objects.create(name=value)
        
        
        self.stdout.write(colored("all symptoms enter successfully.","green"))