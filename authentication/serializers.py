from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = ("PID", 'Name', 'Age', 'DOB', 'gender', 'bg', 'pn', 'Add' )