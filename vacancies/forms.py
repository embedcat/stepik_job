from crispy_forms.layout import Submit
from django import forms
from crispy_forms.helper import FormHelper
from vacancies.models import Application, Company, Vacancy, Resume


class ApplicationForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Отправить отклик'))

        self.helper.label_class = 'mb-1'

    class Meta:
        model = Application
        fields = ['written_username', 'written_phone', 'written_cover_letter', ]
        labels = {
            'written_username': 'Вас зовут',
            'written_phone': 'Ваш телефон',
            'written_cover_letter': 'Сопроводительное письмо',
        }


class CompanyEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Company
        fields = ['name',
                  'location',
                  'description',
                  'employee_count', ]
        labels = {
            'name': 'Название',
            'location': 'География',
            'logo': 'Логотип',
            'description': 'Описание',
            'employee_count': 'Кол-во сотрудников',
        }


class VacancyEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Vacancy
        fields = ['title',
                  'specialty',
                  'skills',
                  'description',
                  'salary_min',
                  'salary_max', ]
        labels = {
            'title': 'Название вакансии',
            'specialty': 'Специализация',
            'skills': 'Требуемые навыки',
            'description': 'Описание вакансии',
            'salary_min': 'Зарплата от',
            'salary_max': 'Зарплата до',
        }


class ResumeEditForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Сохранить'))

    class Meta:
        model = Resume
        fields = [
            'first_name',
            'last_name',
            'status',
            'salary',
            'specialty',
            'education',
            'experience',
            'portfolio',
        ]
        labels = {
            'first_name': 'Имя',
            'last_name': 'Фамилия',
            'status': 'Готовность к работе',
            'salary': 'Ожидаемое вознаграждение',
            'specialty': 'Специализация',
            'education': 'Образование',
            'experience': 'Опыт работы',
            'portfolio': 'Ссылка на портфолио',
        }
