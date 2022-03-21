import random
import string

from django.contrib.auth import authenticate 
from rest_framework import serializers


def get_and_authenticate_supplierAccount(email, password):
    supplierAccount = authenticate(email=email, password=password)
    
    if supplierAccount is None:
        raise serializers.ValidationError(
            "Invalid username/password. Please try again!"
        )
    
    return supplierAccount

def random_chars(x):
    return ''.join(random.choice(string.ascii_uppercase) for x in range(x))

def generate_key():
    return (f"{random.randrange(1, 9)}{random_chars(5)}{random.randrange(1, 9)}{random_chars(2)}" 
            f"{random.randrange(1, 9)}{random_chars(1)}{random.randrange(1, 9)}{random_chars(3)}")

    