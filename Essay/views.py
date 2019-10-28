from django.shortcuts import render
from rest_framework import viewsets
from .models import Essay
from .serializer import EssaySerializer


class EssayViewSet(viewsets.ModelViewSet):
    queryset = Essay.objects.all()
    serializer_class = EssaySerializer
    
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
        
    def get_queryset(self):
        qs = super().get_queryset()

        if self.request.user.is_authenticated:
            qs = qs.filter(author=self.request.user)

        else:
            qs = qs.none()

        return qs