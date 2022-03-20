from django.contrib.auth import authenticate 
from rest_framework import serializers


def get_and_authenticate_supplierAccount(email, password):
    supplierAccount = authenticate(email=email, password=password)
    
    if supplierAccount is None:
        raise serializers.ValidationError(
            "Invalid username/password. Please try again!"
        )
    
    return supplierAccount
    