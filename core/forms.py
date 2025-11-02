from .models import *
from django import forms


class patientForm(forms.ModelForm):
    
    class Meta:
        model = PATIENT
        fields=('picture', 'age', 'gender', )
        
        
        widgets = {
            'gender': forms.Select(attrs={'class':'form-control'})
        }
        