from django.http import HttpResponse
from .models import itc_user_interaction
from .serializers import user_interactionSerializer
from rest_framework import viewsets
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status


# class ApiIndexView(UpdateView):
#     permission_classes = (permissions.AllowAny,)
#
#     def post(self, request, format=None):
#         return Response("ok")
#
class ApiIndexView(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = user_interactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        itc_tables = itc_user_interaction.objects.all()
        serializer = user_interactionSerializer(itc_tables, many=True)
        return Response(serializer.data)

class user_interactionViewSet(viewsets.ModelViewSet):
    queryset = itc_user_interaction.objects.all()
    serializer_class = user_interactionSerializer

def index(request):
    return render(request,'index.html')

def blog(request):
    return render(request,'blog.html')

def buzzlove(request):
    return render(request,'buzzLove.html')

def creative(request):
    return render(request,'creative.html')

def index_all(request):
    return render(request,'index_all.html')

def index_branding(request):
    return render(request,'index_branding.html')

def index_buzzLove(request):
    return render(request,'index_buzzLove.html')

def index_confidential(request):
    return render(request,'index_confidential.html')

def index_web(request):
    return render(request,'index_web.html')

def portfolio(request):
    return render(request,'portfolio.html')

def website(request):
    return render(request,'website.html')



