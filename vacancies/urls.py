from django.urls import path
from vacancies.views import MainView, VacanciesAllView, VacancyView, \
    CompanyView, SpecialitiesView, CompaniesAllView, about_view, CustomLoginView, RegisterView

urlpatterns = [
    path('', MainView.as_view(), name='Main view'),
    path('vacancies/', VacanciesAllView.as_view(), name='All vacancies'),
    path('vacancies/cat/<str:spec_code>', SpecialitiesView.as_view(), name='Speciality view'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='Company card'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name="Vacancy view"),
    path('companies/', CompaniesAllView.as_view(), name='All companies'),
    path('about/', about_view, name='About View'),
    path('login/', CustomLoginView.as_view(), name='Login View'),
    path('register/', RegisterView.as_view(), name='Register View'),
]
