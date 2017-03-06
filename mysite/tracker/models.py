from django.db import models
import datetime

class itc_user_interaction(models.Model):
    user_id = models.IntegerField()
    current_page = models.CharField(max_length=1000)
    buttons_clicked = models.CharField(max_length=100)
    page_visited = models.CharField(max_length=1000)
    coordinates = models.CharField (max_length=25)
    overall_time = models.CharField(max_length=50)
    date_time_of_access = models.DateTimeField(auto_now_add=True)

