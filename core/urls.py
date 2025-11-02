from django.urls import path
from .views import *


urlpatterns = [
    
    path("prediction/new/", PREDICTION_ADD_VIEW.as_view(), name="predictionAdd"),
    path("predictions/list/", PREDICTION_LIST_VIEW.as_view(), name="predictionList"),
    path("prediction/<int:id>/delete/", PEREDICTION_DELETE_VIEW, name="predictionDelete"),
    path("prediction/delete/all/", PEREDICTION_DELETE_ALL_VIEW, name="predictionDeleteAll"),
    path("symptoms/all/", SYMPTOMS_LIST_VIEW.as_view(), name="symptomsList"),
    path("disease/all/", DISEASES_LIST_VIEW.as_view(), name="diseasesList"),
    
    path('patient/profile/',PROFILE_VIEW.as_view(), name="profile"),
    path('patient/edit/',PROFILECreate_VIEW.as_view(), name="profileEdit"),
    
    
]

