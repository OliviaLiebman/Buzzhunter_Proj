from django.contrib import admin

# Register your models here.
from .models import itc_user_interaction, page_interaction, heatmap

admin.site.register(itc_user_interaction)
admin.site.register(page_interaction)
admin.site.register(heatmap)
