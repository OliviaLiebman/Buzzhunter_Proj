from django.http import HttpResponse
# import mySqldb

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")