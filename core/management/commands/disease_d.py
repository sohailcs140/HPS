from django.core.management.base import BaseCommand, CommandError
from termcolor import colored  # for colorful terminal messages
from core.models import DESEASE

class Command(BaseCommand):
    help = "deleting desease"


    def handle(self, *args, **options):
        
        
        
        user_response = input(colored("Do you want to delete disease? (yes/no):", "red"))
        
        if user_response.lower()=="yes":
            
            self.stdout.write(colored("deleting diseases...","green"))
            
            DESEASE.objects.all().delete()
            
            
            self.stdout.write(colored("all diseases deleted successfully.","green"))