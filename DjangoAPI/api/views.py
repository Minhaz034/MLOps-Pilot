from rest_framework import viewsets
from rest_framework.decorators import api_view
from .forms import FeatureForm
from rest_framework.decorators import api_view
from django.core import serializers
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from .models import Features
from .serializer import FeaturesSerializer
from django.contrib import messages
import joblib
import json
import numpy as np
import pandas as pd
from django.shortcuts import render,redirect

# Create your views here.
class FeaturesView(viewsets.ModelViewSet):
    queryset = Features.objects.all()
    serializer_class =  FeaturesSerializer

def status(df):
    try:
        model = joblib.load("/home/aci/PycharmProjects/MLOps-Pilot/DjangoAPI/api/xgb_small_model.sav")
        X = df
        pred = model.predict(X)
        return pred
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)


def FormView(request):
    if request.method == 'POST':
        form = FeatureForm(request.POST or None)

        if form.is_valid():
            age = form.cleaned_data['age']
            installmentSize = form.cleaned_data['installmentSize']
            installment_1 = form.cleaned_data['installment_1']
            installment_2 = form.cleaned_data['installment_2']
            installment_3 = form.cleaned_data['installment_3']
            installment_4 = form.cleaned_data['installment_4']
            installment_5 = form.cleaned_data['installment_5']
            installment_6 = form.cleaned_data['installment_6']
            installment_7 = form.cleaned_data['installment_7']
            installment_8 = form.cleaned_data['installment_8']
            installment_9 = form.cleaned_data['installment_9']
            installment_10 = form.cleaned_data['installment_10']
            installment_11 = form.cleaned_data['installment_11']

            df = pd.DataFrame({
                'age' : [age],
                "installmentSize":[installmentSize],
                "installment_1": [installment_1],
                "installment_2": [installment_2],
                "installment_3": [installment_3],
                "installment_4": [installment_4],
                "installment_5": [installment_5],
                "installment_6": [installment_6],
                "installment_7": [installment_7],
                "installment_8": [installment_8],
                "installment_9": [installment_9],
                "installment_10": [installment_10],
                "installment_11": [installment_11]
            })
            result = status(df)
            return  render(request,'status.html',{"data":result})

    form = FeatureForm()
    return render(request,'form.html',{'form':form})




