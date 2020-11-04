from django.contrib.auth.views import LogoutView
from django.urls import path, include
from rest_framework import routers

from vacancies import apiviews
from vacancies.views import MainView, VacanciesAllView, VacancyView, \
    CompanyView, SpecialitiesView, CompaniesAllView, \
    UserCompanylVacancyListView, UserCompanyVacancyEditView, UserCompanyView, VacancySendApplicationView, \
    about_view, CustomLoginView, RegisterView, UserCompanyCreateView, SearchView, UserResumeView, UserResumeCreateView


router = routers.DefaultRouter()
router.register(r'users', apiviews.UserViewSet)
router.register(r'groups', apiviews.GroupViewSet)
router.register(r'vacancies', apiviews.VacanciesViewSet)
router.register(r'specialties', apiviews.SpecialtyViewSet)
router.register(r'companies', apiviews.CompanyViewSet)
router.register(r'applications', apiviews.ApplicationViewSet)
router.register(r'resumes', apiviews.ResumeViewSet)


urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesAllView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:spec_code>/', SpecialitiesView.as_view(), name='specialty'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company_card'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
    path('companies/', CompaniesAllView.as_view(), name='all_companies'),
    path('about/', about_view, name='about'),
    path('vacancies/<int:vacancy_id>/send/', VacancySendApplicationView.as_view(), name='vacancy_send'),
    path('mycompany/', UserCompanyView.as_view(), name='mycompany'),
    path('mycompany/create', UserCompanyCreateView.as_view(), name='mycompany_create'),
    path('mycompany/vacancies/', UserCompanylVacancyListView.as_view(), name='mycompany_vacancy_list'),
    path('mycompany/vacancies/<int:vacancy_id>/', UserCompanyVacancyEditView.as_view(), name='mycompany_vacancy'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('search/', SearchView.as_view(), name='search'),
    path('myresume/', UserResumeView.as_view(), name='myresume'),
    path('myresume/create/', UserResumeCreateView.as_view(), name='myresume_create'),

    path('api/v1/', include(router.urls)),
]
