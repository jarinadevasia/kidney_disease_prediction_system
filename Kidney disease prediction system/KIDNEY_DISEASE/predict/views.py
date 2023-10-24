from django.shortcuts import render
from .forms import KidneyDiseaseForm
import pandas as pd
import joblib
import os
from django.conf import settings
from django.http import HttpResponse

# Load the trained model

# model = joblib.load("C:\\Users\\MyPc$\\Downloads\\Kidney disease prediction system\\Kidney disease prediction system\\KIDNEY_DISEASE\\predict\\Notebook\\random_forest_model .pkl")

model = joblib.load("C:\\Users\\MyPc$\\Downloads\\Kidney disease prediction system\\Kidney disease prediction system\\KIDNEY_DISEASE\\predict\\Notebook\\random_forest_model.joblib")

def home(request):
    result = None  # Initialize result as None
    if request.method == 'POST':
        form = KidneyDiseaseForm(request.POST)
        if form.is_valid():
            rbc = form.cleaned_data['rbc']
            sg = form.cleaned_data['sg']
            al = form.cleaned_data['al']
            su = form.cleaned_data['su']
            htn = form.cleaned_data['htn']

            # Make prediction
            input_data = pd.DataFrame({
                'Rbc': [rbc],
                'Sg': [sg],
                'Al': [al],
                'Su': [su],
                'Htn': [htn]
            })
            prediction = model.predict(input_data)
            result = "Has Disease" if prediction[0] == 1 else "Not having Disease"

    else:
        form = KidneyDiseaseForm()

    return render(request, 'index.html', {'form': form, 'result': result})
