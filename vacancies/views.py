from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView

from .forms import ApplicationForm, CompanyEditForm, VacancyEditForm
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
        if form.is_valid() and request.user.is_authenticated:
            Application.objects.create(
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
        return render(
            request=request,
            template_name='vacancies/companies.html',
            context={
                'title': 'Лучшие компании',
                'companies': companies,
            })


class MyCompanyView(View):
    def get(self, request):
        company = Company.objects.filter(owner=request.user)[0]
        if company:
            template_name = 'vacancies/company-edit.html'
        else:
            template_name = 'vacancies/company-create.html'

        return render(
            request=request,
            template_name=template_name,
            context={
                'title': 'Моя компания',
                'form': CompanyEditForm(instance=company),
            })

    def post(self, request):
        form = CompanyEditForm(request.POST)
        company = Company.objects.filter(owner=request.user)[0]
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.location = form.cleaned_data['location']
            company.description = form.cleaned_data['description']
            company.employee_count = form.cleaned_data['employee_count']
            company.save()
            return redirect('mycompany')
        return render(
            request=request,
            template_name='vacancies/company-edit.html',
            context={
                'title': 'Моя компания',
                'form': form,
            })


class MyCompanyCreateView(View):
    def get(self, requsest):
        if requsest.user.is_authenticated:
            Company.objects.create(
                name='Название',
                location='Расположение',
                logo='https://place-hold.it/120x60',
                description='Описание',
                employee_count=0,
                owner=requsest.user)
            return redirect('mycompany')
        raise HttpResponseForbidden()


class MyCompanylVacancyListView(View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(company__owner=request.user)
        return render(request=request, template_name='vacancies/vacancy-list.html',
                      context={
                          'title': 'Вакансии компании',
                          'vacancies': vacancies,
                      })


class MyCompanyVacancyEditView(View):
    def get(self, request, vacancy_id):
        vacancy = Vacancy.objects.get(id=vacancy_id)
        applications = Application.objects.filter(vacancy=vacancy)
        return render(
            request=request,
            template_name='vacancies/vacancy-edit.html',
            context={
                'title': 'Редактировать вакансию',
                'vacancy': vacancy,
                'applications': applications,
                'form': VacancyEditForm(instance=vacancy),
            })

    def post(self, request, vacancy_id):
        form = VacancyEditForm(request.POST)
        vacancy = Vacancy.objects.get(id=vacancy_id)

        if form.is_valid():
            vacancy.title = form.cleaned_data['title']
            vacancy.specialty = form.cleaned_data['specialty']
            vacancy.skills = form.cleaned_data['skills']
            vacancy.description = form.cleaned_data['description']
            vacancy.salary_min = int(form.cleaned_data['salary_min'])
            vacancy.salary_max = int(form.cleaned_data['salary_max'])
            vacancy.save()
            return redirect('mycompany_vacancy', vacancy_id=vacancy_id)
        return render(
            request=request,
            template_name='vacancies/company-edit.html',
            context={
                'title': 'Моя компания',
                'form': form,
            })


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
