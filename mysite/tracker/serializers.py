from rest_framework import serializers
from .models import itc_user_interaction, page_interaction, heatmap

class user_interactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = itc_user_interaction
        fields= ('user_id', 'user_name', 'user_email', 'session_id', 'overall_time', 'date_time_of_access', 'percentage_scroll')

class page_interactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = page_interaction
        fields = ('user_id', 'session_id', 'current_page', 'buttons_clicked', 'coordinates')



class heatmapSerializer(serializers.ModelSerializer):

    class Meta:
        model = heatmap
        fields= ('x_coordinate', 'y_coordinate', 'current_page')


