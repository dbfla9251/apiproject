from django.shortcuts import render
from rest_framework import viewsets
from .models import File
from .serializer import FileSerializer


class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)