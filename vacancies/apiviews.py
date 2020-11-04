from django.contrib.auth.models import User, Group
from rest_framework import viewsets, permissions

from vacancies.models import Vacancy, Specialty, Company, Application, Resume
from vacancies.serializers import UserSerializer, GroupSerializer, VacancySerializer, SpecialtySerializer, \
    CompanySerializer, ApplicationSerializer, ResumeSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class VacanciesViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Vacancies
    """
    queryset = Vacancy.objects.all()
    serializer_class = VacancySerializer
    permission_classes = [permissions.IsAuthenticated]


class SpecialtyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Specialties
    """
    queryset = Specialty.objects.all()
    serializer_class = SpecialtySerializer
    permission_classes = [permissions.IsAuthenticated]


class CompanyViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Companies
    """
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]


class ApplicationViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Applications
    """
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.IsAuthenticated]


class ResumeViewSet(viewsets.ModelViewSet):
    """
    API endpoint for Resumes
    """
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
    permission_classes = [permissions.IsAuthenticated]
