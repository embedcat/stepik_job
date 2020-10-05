from django.shortcuts import render
from django.views.generic import View


class MainView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='vacancies/index.html',
                      context={
                          'title': '',
                      })


class SpecialitiesView(View):
    def get(self, request, spec, *args, **kwargs):
        return render(request=request, template_name='vacancies/search.html',
                      context={
                          'title': 'Вакансии | ',
                      })


class CompanyView(View):
    def get(self, request, company_id, *args, **kwargs):
        return render(request=request, template_name='vacancies/company.html',
                      context={
                          'title': 'Компания | ',
                      })


class VacanciesAllView(View):
    def get(self, request, *args, **kwargs):
        return render(request=request, template_name='vacancies/vacancies.html',
                      context={
                          'title': 'Вакансии | ',
                      })


class VacancyView(View):
    def get(self, request, vacancy_id, *args, **kwargs):
        return render(request=request, template_name='vacancies/vacancy.html',
                      context={
                          'title': 'Вакансия | ',
                      })


def page_not_found_view(request, exception):
    return render(request=request, template_name='vacancies/error.html', status=404, context={'code': '404'})


def error_view(request):
    return render(request=request, template_name='vacancies/error.html', status=500, context={'code': '500'})
