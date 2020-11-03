from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, CreateView
from django.db.models import Q

from .forms import ApplicationForm, CompanyEditForm, VacancyEditForm, ResumeEditForm
from .models import Specialty, Vacancy, Company, Application, Resume


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
            template_name='vacancies/spec-vacancies.html',
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


class UserCompanyView(LoginRequiredMixin, View):
    def get(self, request):
        company = Company.objects.filter(owner=request.user).first()
        if company is None:
            template_name = 'vacancies/company-create.html'
            form = CompanyEditForm()
        else:
            template_name = 'vacancies/company-edit.html'
            form = CompanyEditForm(instance=company)

        return render(
            request=request,
            template_name=template_name,
            context={
                'title': 'Моя компания',
                'form': form,
            })

    def post(self, request):
        form = CompanyEditForm(request.POST, request.FILES)
        company = Company.objects.filter(owner=request.user).first()
        if form.is_valid():
            company.name = form.cleaned_data['name']
            company.location = form.cleaned_data['location']
            company.logo = form.cleaned_data['logo']
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


class UserCompanyCreateView(LoginRequiredMixin, View):
    def get(self, request):
        company = Company.objects.filter(owner=request.user).first()
        if company is None:
            return render(
                request=request,
                template_name='vacancies/company-edit.html',
                context={
                    'title': 'Моя компания',
                    'form': CompanyEditForm(),
                })
        return redirect('mycompany')

    def post(self, request):
        form = CompanyEditForm(request.POST, request.FILES)
        if form.is_valid():
            Company.objects.create(
                name=form.cleaned_data['name'],
                location=form.cleaned_data['location'],
                logo=form.cleaned_data['logo'],
                description=form.cleaned_data['description'],
                employee_count=form.cleaned_data['employee_count'],
                owner=request.user
            )
            return redirect('mycompany')
        return render(
            request=request,
            template_name='vacancies/company-edit.html',
            context={
                'title': 'Моя компания',
                'form': form,
            })


class UserCompanylVacancyListView(LoginRequiredMixin, View):
    def get(self, request):
        vacancies = Vacancy.objects.filter(company__owner=request.user)
        return render(request=request, template_name='vacancies/vacancy-list.html',
                      context={
                          'title': 'Вакансии компании',
                          'vacancies': vacancies,
                      })


class UserCompanyVacancyEditView(LoginRequiredMixin, View):
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


class SearchView(View):
    def get(self, request):
        vacancies = Vacancy.objects.none
        query = ''
        if 'q' in request.GET:
            query = request.GET.get('q').strip()
            vacancies = Vacancy.objects.filter(
                Q(title__icontains=query) | Q(description__icontains=query) | Q(skills__icontains=query))
        return render(
            request=request,
            template_name='vacancies/search.html',
            context={
                'title': 'Поиск',
                'vacancies': vacancies,
                'query': query,
            })


class UserResumeView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            resume = Resume.objects.get(user=request.user)
            template_name = 'vacancies/resume-edit.html'
            form = ResumeEditForm(instance=resume)
        except Resume.DoesNotExist:
            template_name = 'vacancies/resume-create.html'
            form = None

        return render(
            request=request,
            template_name=template_name,
            context={
                'title': 'Моё резюме',
                'form': form,
            })

    def post(self, request):
        form = ResumeEditForm(request.POST)
        try:
            resume = Resume.objects.get(user=request.user)
        except Resume.DoesNotExist:
            return redirect('main')
        if form.is_valid():
            resume.first_name = form.cleaned_data['first_name']
            resume.last_name = form.cleaned_data['last_name']
            resume.status = form.cleaned_data['status']
            resume.salary = form.cleaned_data['salary']
            resume.specialty = form.cleaned_data['specialty']
            resume.education = form.cleaned_data['education']
            resume.experience = form.cleaned_data['experience']
            resume.portfolio = form.cleaned_data['portfolio']
            resume.save()
            return redirect('myresume')
        return render(
            request=request,
            template_name='vacancies/resume-edit.html',
            context={
                'title': 'Моё резюме',
                'form': form,
            })


class UserResumeCreateView(LoginRequiredMixin, View):
    def get(self, request):
        try:
            Resume.objects.get(user=request.user)
            return redirect('myresume')
        except Resume.DoesNotExist:
            return render(
                request=request,
                template_name='vacancies/resume-edit.html',
                context={
                    'title': 'Моё резюме',
                    'form': ResumeEditForm(),
                })

    def post(self, request):
        form = ResumeEditForm(request.POST)
        if form.is_valid():
            Resume.objects.create(
                user=request.user,
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
                status=form.cleaned_data['status'],
                salary=form.cleaned_data['salary'],
                specialty=form.cleaned_data['specialty'],
                education=form.cleaned_data['education'],
                experience=form.cleaned_data['experience'],
                portfolio=form.cleaned_data['portfolio'],
            )
            return redirect('myresume')
        return render(
            request=request,
            template_name='vacancies/resume-edit.html',
            context={
                'title': 'Моё резюме',
                'form': form,
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
