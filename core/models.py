from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

GENDER_CHOICES = (('0',"FeMale"), ('1',"Male"),('2', "Other"))

class USER(AbstractUser):
    pass

class PATIENT(models.Model):
    
    user = models.OneToOneField(to=USER, on_delete=models.CASCADE,related_name="profile")
    picture = models.ImageField(upload_to="profile/images/", null=True, blank=True)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)


class SYMPTOMS(models.Model):
    name = models.CharField(max_length=50, unique=True)


class DESEASE(models.Model):
    name = models.CharField(max_length=50, unique=True)



class PREDICTION(models.Model):
    
    patient = models.ForeignKey(to=USER, on_delete=models.CASCADE, related_name="predictions")
    desease = models.ForeignKey(to=DESEASE, on_delete=models.CASCADE)
    createAt = models.DateTimeField(auto_now=False, auto_now_add=True)
    updateAt = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        ordering = ['-createAt']
    
    
class SYMPTOMS_in_PREDICTION(models.Model):
    
    prediction = models.ForeignKey(to=PREDICTION, on_delete=models.CASCADE, related_name="symptoms")
    symptom = models.ForeignKey(to=SYMPTOMS, on_delete=models.CASCADE)
    






