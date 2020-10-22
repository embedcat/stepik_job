from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView

from .forms import ApplicationForm
from .models import Specialty, Vacancy, Company, Application


class MainView(View):
    def get(self, request):
        specs = Specialty.objects.all()
        companies = Company.objects.all()
        return render(
            request=request,
            template_name='vacancies/index.html',
            context={
                'title': 'Джуманджи',
                'specs': specs,
                'companies': companies,
            },
        )


class SpecialitiesView(View):
    def get(self, request, spec_code):
        spec = Specialty.objects.get(code=spec_code)
        return render(
            request=request,
            template_name='vacancies/search.html',
            context={
                'title': f'Вакансии {spec.title}',
                'spec': spec,
            },
        )


class CompanyView(View):
    def get(self, request, company_id):
        company = Company.objects.get(id=company_id)
        return render(
            request=request,
            template_name='vacancies/company.html',
            context={
                'title': f'Компания {company.name}',
                'company': company,
            },
        )


class VacanciesAllView(View):
    def get(self, request):
        specs = Specialty.objects.all()
        return render(request=request, template_name='vacancies/vacancies.html',
                      context={
                          'title': 'Вакансии',
                          'specs': specs,
                      })


class VacancyView(View):
    def get(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        return render(
            request=request,
            template_name='vacancies/vacancy.html',
            context={
                'title': 'Вакансия',
                'vacancy': vacancy,
                'form': ApplicationForm(),
            })

    def post(self, request, vacancy_id):
        form = ApplicationForm(request.POST)
        vacancy = Vacancy.objects.get(id=vacancy_id)
        if form.is_valid():
            application = Application.objects.create(
                written_username=form.cleaned_data['written_username'],
                written_phone=form.cleaned_data['written_phone'],
                written_cover_letter=form.cleaned_data['written_cover_letter'],
                vacancy=vacancy,
                user=request.user,
            )
            return redirect('vacancy_send', vacancy_id=vacancy_id)
        return render(
            request=request,
            template_name='vacancies/vacancy.html',
            context={
                'title': 'Вакансия',
                'vacancy': vacancy,
                'form': form,
            })


class CompaniesAllView(View):
    def get(self, request):
        companies = Company.objects.all()
        return render(request=request, template_name='vacancies/companies.html',
                      context={
                          'title': 'Лучшие компании',
                          'companies': companies,
                      })


class MyCompanyView(View):
    def get(self, request):
        return render(request=request, template_name='vacancies/company-create.html',
                      context={
                          'title': 'Моя компания',
                      })


class MyCompanylVacancyListView(View):
    def get(self, request):
        return render(request=request, template_name='vacancies/vacancy-list.html',
                      context={
                          'title': 'Вакансии компании',
                      })


class MyCompanyVacancyEditView(View):
    def get(self, request, vacancy_id):
        return render(request=request, template_name='vacancies/vacancy-edit.html')


class VacancySendApplicationView(View):
    def get(self, request, vacancy_id):
        return render(request=request, template_name='vacancies/sent.html',
                      context={
                          'title': 'Отклик отправлен',
                          'vacancy_id': int(vacancy_id),
                      })


class CustomLoginView(LoginView):
    redirect_authenticated_user = True
    template_name = 'vacancies/login.html'
    extra_context = {
        'title': 'Вход',
    }


class RegisterView(CreateView):
    form_class = UserCreationForm
    success_url = '/login'
    template_name = 'vacancies/register.html'
    extra_context = {
        'title': 'Регистрация',
    }


def about_view(request):
    return render(request=request, template_name='vacancies/about.html')


def page_not_found_view(request, exception):
    return render(request=request, template_name='vacancies/error.html', status=404, context={'code': '404'})


def error_view(request):
    return render(request=request, template_name='vacancies/error.html', status=500, context={'code': '500'})
