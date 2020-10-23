from django import forms
from vacancies.models import Application, Company, Vacancy


class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter', ]


class CompanyEditForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name',
                  'location',
                  'logo',
                  'description',
                  'employee_count', ]


class VacancyEditForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = ['title',
                  'specialty',
                  'skills',
                  'description',
                  'salary_min',
                  'salary_max', ]
