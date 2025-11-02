from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from .models import *
from django.views import View
from HPS.main import all_symptoms
from render_block import render_block_to_string
from time import sleep
from django.http import HttpResponse
from HPS.main import predictDisease
from django.db import transaction
from django.views.generic import ListView
from django.contrib import messages
from .forms import patientForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class PREDICTION_ADD_VIEW(LoginRequiredMixin, View):
    
    def get(self, request):
        
        context ={"symptoms":all_symptoms, 'active':'n'}
        return render(request, "core1/newPrediction.html",context)
        
    def post(self, request):
        
            
        try:

            with transaction.atomic():
                symptoms = request.POST.getlist('symptoms')
                output = predictDisease(symptoms)
                
                
                disease = DESEASE.objects.get(name=output.get('disease'))
                # Insertion in prediction
                prediction = PREDICTION.objects.create(patient=request.user, desease=disease)
                
                # insertin in symptoms prediction
                message = output.get("message")
                for symptom in symptoms:
                    
                    dataBaseSymptom = SYMPTOMS.objects.get(name=symptom)
                    
                    SYMPTOMS_in_PREDICTION.objects.create(prediction=prediction, symptom=dataBaseSymptom)
        except:
        
            message = "Opp's something went wrong?🤔"
        
        
        response = render_block_to_string("core1/newPrediction.html","output", {'message':message,'disease':output.get('disease')})
        sleep(3)
        return HttpResponse(response)



class PREDICTION_LIST_VIEW(LoginRequiredMixin,ListView):
    
    model = PREDICTION
    template_name = "core1/predictions.html"
    
    context_object_name = "predictions"
    
    def get_queryset(self):

        return PREDICTION.objects.filter(patient=self.request.user)

    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['active']='h'
        return context

@login_required
def PEREDICTION_DELETE_VIEW(request, id):
    
    try:
        PREDICTION.objects.get(id=id).delete()
    
        messages.success(request,"record deleted succssfully")

    except:
       messages.error(request,"some thing went wrong")
    
    context = {
        'predictions':PREDICTION.objects.all(),
    }
    
    return render(request, "core1/includes/table.html", context)

@login_required
def PEREDICTION_DELETE_ALL_VIEW(request):
    
    try:
        PREDICTION.objects.all().delete()
    
        messages.success(request,"All recods  deleted")

    except:
       messages.error(request,"some thing went wrong")
    context = {
        'predictions':PREDICTION.objects.all(),
    }
    return render(request, "core1/includes/table.html", context)




class SYMPTOMS_LIST_VIEW(LoginRequiredMixin,ListView):
    
    model = SYMPTOMS
    template_name = "core1/symptoms.html"
    
    context_object_name = "symptoms"
    
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['active']='as'
        return context
    
class DISEASES_LIST_VIEW(LoginRequiredMixin,ListView):
    
    model = DESEASE
    template_name = "core1/disease.html"
    
    context_object_name = "diseases"
    def get_context_data(self, **kwargs: Any):
        context = super().get_context_data(**kwargs)
        context['active']='ad'
        return context

class PROFILE_VIEW(LoginRequiredMixin,View):
    
    def get(self, request):
        
        patient = PATIENT.objects.filter(user=request.user).first() or None
        form = patientForm(instance=patient)
        context = {'form':form}
        
        
        return render(request, 'core1/profile.html', context)
    
    def post(self, request):
        
        patient = PATIENT.objects.filter(user=request.user).first() or None
        
        if patient is not None:
            
            form = patientForm(instance=patient, data=request.POST, files=request.FILES)
        else:
            form = patientForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            patient.user.first_name=request.POST.get('first_name')
            patient.user.last_name=request.POST.get('last_name')
            patient.user.save()
           
            messages.success(request, "profile updated success fully")
        else:
            messages.error(request, "some thing went wrong")
            
        return redirect('profile')


class PROFILECreate_VIEW(LoginRequiredMixin,View):
    
    def get(self, request):
        
        patient = PATIENT.objects.filter(user=request.user).first() or None
        form = patientForm(instance=patient)
        context = {'form':form}
        
        
        return render(request, 'core1/profileEdit.html', context)
    
    
    def post(self, request):
        
        patient = PATIENT.objects.filter(user=request.user).first() or None
        
        if patient is not None:
            
            form = patientForm(instance=patient, data=request.POST, files=request.FILES)
        else:
            form = patientForm(data=request.POST, files=request.FILES)
        
        if form.is_valid():
            
            patient = form.save(commit=False)
            patient.user = request.user
            patient.save()
            patient.user.first_name=request.POST.get('first_name')
            patient.user.last_name=request.POST.get('last_name')
            

            patient.user.save()
           
            messages.success(request, "profile updated success fully")
        else:
            messages.error(request, "some thing went wrong")
            
        return redirect('profile')