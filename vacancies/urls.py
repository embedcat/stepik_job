from django.urls import path
from vacancies.views import MainView, VacanciesAllView, VacancyView, CompanyView, SpecialitiesView

urlpatterns = [
    path('', MainView.as_view(), name='Main view'),
    path('vacancies', VacanciesAllView.as_view(), name='All vacancies'),
    path('vacancies/cat/<str:spec>', SpecialitiesView.as_view(), name='Speciality view'),
    path('companies/<int:company_id>', CompanyView.as_view(), name='Company card'),
    path('vacancies/<int:vacancy_id>', VacancyView.as_view(), name="Vacancy view"),
]
