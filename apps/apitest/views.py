from rest_framework import viewsets
from .models import Project, Host
from rest_framework.permissions import IsAuthenticated
from .serializers import ProjectSerializer, HostSerializer
from apps.test_auth.authorizations import JWTAuthentication


# Create your views here.
class ProjectViewSets(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = ProjectSerializer


class HostViewSets(viewsets.ModelViewSet):
    queryset = Host.objects.all()
    authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]
    serializer_class = HostSerializer
