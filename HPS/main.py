import joblib
import numpy as np
from django.conf import settings
import os
import random
import warnings

# Function for preprocessing user input and creating a binary vector
def preprocess_input(input_text, all_symptoms):
    # Initialize a binary vector with zeros
    binary_vector = np.zeros(len(all_symptoms))

    # Split the input string by commas to get a list of symptoms
    input_symptoms = input_text.split(',')
    # Convert all symptom names to lowercase for case-insensitive matching
    all_symptoms_lower = [symptom.lower() for symptom in all_symptoms]

    # Set the corresponding elements to 1 for symptoms present in the input
    for symptom in input_symptoms:
        if symptom.lower() in all_symptoms_lower:
            index = all_symptoms_lower.index(symptom.lower())
            binary_vector[index] = 1

    
    return binary_vector

# List of all  symptoms 
all_symptoms = [
    "itching", "skin_rash", "nodal_skin_eruptions", "continuous_sneezing", "shivering", "chills", "joint_pain", "stomach_pain", "acidity",
    "ulcers_on_tongue", "muscle_wasting", "vomiting", "burning_micturition", "spotting_ urination", "fatigue", "weight_gain", "anxiety", "cold_hands_and_feets",
    "mood_swings", "weight_loss", "restlessness", "lethargy", "patches_in_throat", "irregular_sugar_level", "cough", "high_fever", "sunken_eyes",
    "breathlessness", "sweating", "dehydration", "indigestion", "headache", "yellowish_skin", "dark_urine", "nausea", "loss_of_appetite", "pain_behind_the_eyes",
    "back_pain", "constipation", "abdominal_pain", "diarrhoea", "mild_fever", "yellow_urine", "yellowing_of_eyes", "acute_liver_failure", "fluid_overload",
    "swelling_of_stomach", "swelled_lymph_nodes", "malaise", "blurred_and_distorted_vision", "phlegm", "throat_irritation", "redness_of_eyes",
    "sinus_pressure", "runny_nose", "congestion", "chest_pain", "weakness_in_limbs", "fast_heart_rate", "pain_during_bowel_movements", "pain_in_anal_region",
    "bloody_stool", "irritation_in_anus", "neck_pain", "dizziness", "cramps", "bruising", "obesity", "swollen_legs", "swollen_blood_vessels",
    "puffy_face_and_eyes", "enlarged_thyroid", "brittle_nails", "swollen_extremeties", "excessive_hunger", "extra_marital_contacts", "drying_and_tingling_lips",
    "slurred_speech", "knee_pain", "hip_joint_pain", "muscle_weakness", "stiff_neck", "swelling_joints", "movement_stiffness", "spinning_movements",
    "loss_of_balance", "unsteadiness", "weakness_of_one_body_side", "loss_of_smell", "bladder_discomfort", "foul_smell_of urine", "continuous_feel_of_urine",
    "passage_of_gases", "internal_itching", "toxic_look_(typhos)", "depression", "irritability", "muscle_pain", "altered_sensorium", "red_spots_over_body",
    "belly_pain", "abnormal_menstruation", "dischromic _patches", "watering_from_eyes", "increased_appetite", "polyuria", "family_history", "mucoid_sputum",
    "rusty_sputum", "lack_of_concentration", "visual_disturbances", "receiving_blood_transfusion", "receiving_unsterile_injections", "coma",
    "stomach_bleeding", "distention_of_abdomen", "history_of_alcohol_consumption", "fluid_overload", "blood_in_sputum", "prominent_veins_on_calf",
    "palpitations", "painful_walking", "pus_filled_pimples", "blackheads", "scurring", "skin_peeling", "silver_like_dusting", "small_dents_in_nails",
    "inflammatory_nails", "blister", "red_sore_around_nose", "yellow_crust_ooze"
]



# Dictionary to map binary labels to disease names for all provided diseases
disease_mapping = {
    0: "Fungal infection",
    1: "Allergy",
    2: "GERD",
    3: "Chronic cholestasis",
    4: "Drug Reaction",
    5: "Peptic ulcer disease",
    6: "AIDS",
    7: "Diabetes",
    8: "Gastroenteritis",
    9: "Bronchial Asthma",
    10: "Hypertension",
    11: "Migraine",
    12: "Cervical spondylosis",
    13: "Paralysis (brain hemorrhage)",
    14: "Jaundice",
    15: "Malaria",
    16: "Chicken pox",
    17: "Dengue",
    18: "Typhoid",
    19: "Hepatitis A",
    20: "Hepatitis B",
    21: "Hepatitis C",
    22: "Hepatitis D",
    23: "Hepatitis E",
    24: "Alcoholic hepatitis",
    25: "Tuberculosis",
    26: "Common Cold",
    27: "Pneumonia",
    28: "Dimorphic hemorrhoids (piles)",
    29: "Heart attack",
    30: "Varicose veins",
    31: "Hypothyroidism",
    32: "Hyperthyroidism",
    33: "Hypoglycemia",
    34: "Osteoarthristis",
    35: "Arthritis",
    36: "(vertigo) Paroxysmal Positional Vertigo",
    37: "Acne",
    38: "Urinary tract infection",
    39: "Psoriasis",
    40: "Impetigo"
}


file = os.path.join(settings.BASE_DIR, 'disease-prediction-model.joblib')

model = joblib.load(file)  


# Function for predicting disease
def predict_disease(input_binary_vector):
    
     
    # Make predictions using the model
    binary_prediction = model.predict([input_binary_vector])[0]  # Assuming a single input example

    # Map the binary prediction to a disease name using the dictionary
    predicted_disease = disease_mapping.get(binary_prediction)

    return predicted_disease


disease_name = "__name__"

messages = [
    f"It seems that you are experiencing symptoms related to {disease_name} disease. Please consider consulting a healthcare professional for an accurate diagnosis and guidance on managing this condition.",
    f"If you suspect you might have {disease_name} disease, it's essential to reach out to a medical expert who can assess your symptoms and recommend the appropriate steps for your health.",
    f"Experiencing symptoms that align with {disease_name} disease can be concerning. I recommend seeking medical attention to get a clear understanding of your health and potential treatment options.",
    f"I'm sorry to hear that you may be dealing with {disease_name} disease. Remember, timely consultation with a healthcare provider is crucial in addressing any health concerns.",
    f"Your health is important. If you suspect {disease_name} disease, I urge you to schedule an appointment with a healthcare professional to discuss your symptoms and get the necessary care.",
    f"It's important not to ignore any signs of {disease_name} disease. Please consider reaching out to a medical expert to discuss your condition and explore available treatments.",
    f"If you suspect {disease_name} disease, it's advisable to consult with a healthcare specialist who can provide you with accurate information and guidance tailored to your situation.",
    f"Dealing with symptoms that resemble {disease_name} disease can be challenging. Please prioritize your well-being and consult with a healthcare professional for assistance.",
    f"I'm here to encourage you to take your health seriously. If you suspect {disease_name} disease, seek professional medical advice to address your concerns.",
    f"While I'm not a medical professional, I recommend that you consider discussing your symptoms and concerns related to {disease_name} disease with a healthcare expert.",
    f"Experiencing symptoms of {disease_name} disease can be distressing. I suggest contacting a healthcare provider who can provide you with a comprehensive evaluation and treatment plan.",
    f"Your health is precious. If you're worried about {disease_name} disease, consult with a healthcare specialist to gain insights into your condition and available treatment options.",
    f"I'm truly sorry to hear that you may be facing {disease_name} disease. Please seek the guidance of a healthcare expert to address your health concerns.",
    f"It's important to be proactive about your health. If you suspect {disease_name} disease, consider scheduling a consultation with a healthcare professional for proper evaluation.",
    f"Experiencing symptoms associated with {disease_name} disease can be overwhelming. Connect with a healthcare expert to discuss your condition and receive appropriate care.",
    f"Dealing with potential {disease_name} disease symptoms can be worrisome. I encourage you to consult with a healthcare provider for accurate information and guidance.",
    f"Your health should always come first. If you suspect {disease_name} disease, please prioritize seeking advice from a healthcare specialist.",
    f"I want to stress the importance of addressing health concerns. If you believe you may have {disease_name} disease, consult with a healthcare expert to explore your options.",
    f"It's crucial to take your health seriously. If you think you may have {disease_name} disease, reach out to a medical professional to assess your condition.",
    f"Experiencing symptoms that resemble {disease_name} disease can be unsettling. Connect with a healthcare specialist who can provide you with the necessary guidance and support.",
    f"Your health is invaluable. If you have concerns about {disease_name} disease, I recommend consulting with a healthcare provider for a thorough evaluation.",
    f"I'm sorry to hear that you might be facing {disease_name} disease. Please consider seeking advice from a healthcare expert to address your health worries.",
    f"Your well-being is of utmost importance. If you suspect {disease_name} disease, consult with a healthcare specialist for accurate information and guidance.",
    f"Experiencing symptoms associated with {disease_name} disease can be challenging. I encourage you to reach out to a healthcare provider to discuss your concerns.",
    f"Taking care of your health is essential. If you believe you may have {disease_name} disease, consult with a medical professional to explore your options.",
    f"It's crucial to prioritize your health and well-being. If you have concerns about {disease_name} disease, I recommend seeking advice from a healthcare expert.",
    f"I understand that facing potential {disease_name} disease symptoms can be daunting. Connect with a healthcare specialist who can provide you with the necessary guidance and support.",
    f"Your health is irreplaceable. If you're worried about {disease_name} disease, consult with a healthcare provider for a comprehensive evaluation and treatment plan.",
    f"I'm truly sorry to hear that you may be dealing with {disease_name} disease. Please seek the expertise of a healthcare expert to address your health concerns.",
    f"Prioritizing your health is essential. If you suspect {disease_name} disease, consider consulting with a healthcare specialist for proper evaluation and guidance.",
    f"Experiencing symptoms that resemble {disease_name} disease can be overwhelming. Connect with a healthcare provider who can provide you with accurate information and support.",
    f"Your well-being matters. If you have concerns about {disease_name} disease, I recommend consulting with a medical professional to assess your condition.",
    f"I'm sorry to hear that you might be facing {disease_name} disease. Please consider reaching out to a healthcare expert to address your health worries.",
    f"Taking care of your health is a top priority. If you suspect {disease_name} disease, consult with a healthcare specialist for accurate information and guidance.",
    f"It's important to address health concerns promptly. If you believe you may have {disease_name} disease, consult with a medical professional to explore your options.",
    f"I understand that facing potential {disease_name} disease symptoms can be challenging. Connect with a healthcare specialist who can provide you with the necessary guidance and support.",
    f"Your health is priceless. If you're concerned about {disease_name} disease, consult with a healthcare provider for a comprehensive evaluation and treatment plan.",
    f"I'm truly sorry to hear that you may be dealing with {disease_name} disease. Please seek the expertise of a healthcare expert to address your health concerns.",
    f"Your well-being is paramount. If you suspect {disease_name} disease, consider consulting with a healthcare specialist for proper evaluation and guidance.",
    f"Experiencing symptoms that resemble {disease_name} disease can be daunting. Connect with a healthcare provider who can provide you with accurate information and support.",
    f"Prioritizing your health is essential. If you have concerns about {disease_name} disease, I recommend consulting with a medical professional to assess your condition.",
]



def predictDisease(user_input:list[str]):
    
    with warnings.catch_warnings():
        
        warnings.filterwarnings("ignore")
        
        filter_input = ','.join(user_input)
        input_binary_vector = preprocess_input(filter_input, all_symptoms)
        binary_prediction = model.predict([input_binary_vector])[0]
        predicted_disease = disease_mapping.get(binary_prediction)
        
        
        index = random.randint(0, len(messages) - 1)
        
        message = messages[index]
        message = message.replace("__name__",f"{binary_prediction}")
        output = {'message':message, 'disease': binary_prediction}
        return output