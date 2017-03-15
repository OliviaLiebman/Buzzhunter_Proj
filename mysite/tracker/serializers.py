from rest_framework import serializers
from .models import itc_user_interaction, page_interaction

class user_interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = itc_user_interaction
        fields= ('user_id', 'overall_time', 'date_time_of_access', 'session_id')

class page_interactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = page_interaction
        fields= ('user_id', 'current_page', 'buttons_clicked', 'coordinates')
        # fields= ('user_id', 'session_id', 'current_page', 'buttons_clicked', 'coordinates')


