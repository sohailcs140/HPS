from django.core.management.base import BaseCommand, CommandError
from termcolor import colored  # for colorful terminal messages
from core.models import SYMPTOMS

class Command(BaseCommand):
    help = "deleting symptoms"


    def handle(self, *args, **options):
        
        
        
        user_response = input(colored("Do you want to delete symptoms? (yes/no):", "red"))
        
        if user_response.lower()=="yes":
            
            self.stdout.write(colored("deleting symptoms...","green"))
            
            SYMPTOMS.objects.all().delete()
            
            
            self.stdout.write(colored("all symptoms deleted successfully.","green"))