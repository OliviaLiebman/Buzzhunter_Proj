from django.http import HttpResponse
from .models import itc_user_interaction, page_interaction, heatmap
from .serializers import user_interactionSerializer, page_interactionSerializer, heatmapSerializer
from rest_framework import viewsets
from django.views.generic.edit import UpdateView
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework import status


class ApiIndexView1(APIView):
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


class ApiIndexView2(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = page_interactionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        itc_tables = page_interaction.objects.all()
        serializer = page_interactionSerializer(itc_tables, many=True)
        return Response(serializer.data)


class page_interactionViewSet(viewsets.ModelViewSet):
    queryset = page_interaction.objects.all()
    serializer_class = page_interactionSerializer


class ApiIndexView3(APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = heatmapSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, format=None):
        itc_tables = heatmap.objects.all()
        serializer = heatmapSerializer(itc_tables, many=True)
        return Response(serializer.data)


class heatmapViewSet(viewsets.ModelViewSet):
    queryset = heatmap.objects.all()
    serializer_class = heatmapSerializer

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

def portfolio(request):
    return render(request,'portfolio.html')

def website(request):
    return render(request,'website.html')

def dashboard(request):
    return render(request,'dashboard.html')

def heatmap_website(request):
    return render(request,'heatmap_website.html')
