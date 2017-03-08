from rest_framework import serializers
from .models import itc_user_interaction

class user_interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = itc_user_interaction
        fields= '__all__'
