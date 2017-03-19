from django.db import models
import datetime


class itc_user_interaction(models.Model):
    user_id = models.CharField(max_length = 100)
    user_name = models.CharField(max_length= 100, default="User")
    user_email = models.CharField(max_length= 100, default="Email")
    session_id= models.IntegerField(default= 1)
    overall_time = models.CharField(max_length=100, default= "N/A")
    date_time_of_access = models.DateTimeField(auto_now_add=True)
    percentage_scroll = models.CharField(max_length = 100, default = "No Scroll")

class page_interaction (models.Model):
    user_id = models.CharField(max_length = 100)
    session_id = models.IntegerField(default= 1)
    current_page = models.CharField(max_length=1000)
    buttons_clicked = models.TextField(default=False, blank=True)
    coordinates = models.CharField(max_length=25)