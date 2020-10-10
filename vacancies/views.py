from django.shortcuts import render
from django.views.generic import View
from .models import Specialty, Vacancy, Company


class MainView(View):
    def get(self, request, *args, **kwargs):
        specs = Specialty.objects.all()
        companies = Company.objects.all()
        return render(request=request, template_name='vacancies/index.html',
                      context={
                          'title': '',
                          'specs': specs,
                          'companies': companies,
                      })


class SpecialitiesView(View):
    def get(self, request, spec_code, *args, **kwargs):
        spec = Specialty.objects.get(code=spec_code)
        return render(request=request, template_name='vacancies/search.html',
                      context={
                          'title': f'Вакансии {spec.title} | ',
                          'spec': spec,
                      })


class CompanyView(View):
    def get(self, request, company_id, *args, **kwargs):
        company = Company.objects.get(id=company_id)
        return render(request=request, template_name='vacancies/company.html',
                      context={
                          'title': f'Компания {company.name} | ',
                          'company': company,
                      })


class VacanciesAllView(View):
    def get(self, request, *args, **kwargs):
        specs = Specialty.objects.all()
        return render(request=request, template_name='vacancies/vacancies.html',
                      context={
                          'title': 'Вакансии | ',
                          'specs': specs,
                      })


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        return render(request=request, template_name='vacancies/vacancy.html',
                      context={
                          'title': 'Вакансия | ',
                          'vacancy': vacancy,
                      })


class CompaniesAllView(View):
    def get(self, request, *args, **kwargs):
        companies = Company.objects.all()
        return render(request=request, template_name='vacancies/companies.html',
                      context={
                          'title': 'Лучшие компании | ',
                          'companies': companies,
                      })


class LoginView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='vacancies/login.html')


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='vacancies/register.html')


def about_view(request):
    return render(request=request, template_name='vacancies/about.html')


def page_not_found_view(request, exception):
    return render(request=request, template_name='vacancies/error.html', status=404, context={'code': '404'})


def error_view(request):
    return render(request=request, template_name='vacancies/error.html', status=500, context={'code': '500'})
