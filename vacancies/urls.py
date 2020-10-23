from django.contrib.auth.views import LogoutView
from django.urls import path
from vacancies.views import MainView, VacanciesAllView, VacancyView, \
    CompanyView, SpecialitiesView, CompaniesAllView, \
    MyCompanylVacancyListView, MyCompanyVacancyEditView, MyCompanyView, VacancySendApplicationView, \
    about_view, CustomLoginView, RegisterView, MyCompanyCreateView

urlpatterns = [
    path('', MainView.as_view(), name='main'),
    path('vacancies/', VacanciesAllView.as_view(), name='all_vacancies'),
    path('vacancies/cat/<str:spec_code>/', SpecialitiesView.as_view(), name='specialty'),
    path('companies/<int:company_id>/', CompanyView.as_view(), name='company_card'),
    path('vacancies/<int:vacancy_id>/', VacancyView.as_view(), name='vacancy'),
    path('companies/', CompaniesAllView.as_view(), name='all_companies'),
    path('about/', about_view, name='about'),
    path('vacancies/<int:vacancy_id>/send/', VacancySendApplicationView.as_view(), name='vacancy_send'),
    path('mycompany/', MyCompanyView.as_view(), name='mycompany'),
    path('mycompany/create', MyCompanyCreateView.as_view(), name='mycompany_create'),
    path('mycompany/vacancies/', MyCompanylVacancyListView.as_view(), name='mycompany_vacancy_list'),
    path('mycompany/vacancies/<int:vacancy_id>/', MyCompanyVacancyEditView.as_view(), name='mycompany_vacancy'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
]
