from projects.models import Project
from rest_framework import viewsets, permissions
from .serializers import ProjectSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_class = [permissions.AllowAny]
    serializer_class = ProjectSerializer

#comentario para poder hacer un commit lpm