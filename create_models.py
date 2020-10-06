import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from vacancies.models import Vacancy, Specialty, Company
import data


if __name__ == '__main__':
    for spec in data.specialties:
        s = Specialty(code=spec['code'], title=spec['title'], picture=f'static/specialties/specty_{spec["code"]}.png')
        s.save()

    for company in data.companies:
        c = Company(name=company['title'], location='', logo='', description='', employee_count=0)
        c.save()

    for vacancy in data.jobs:
        s = Specialty.objects.get(code=vacancy['cat'])
        c = Company.objects.get(name=vacancy['company'])
        v = Vacancy(title=vacancy['title'],
                    specialty=s,
                    company=c,
                    skills='',
                    description=vacancy['desc'],
                    salary_min=int(vacancy['salary_from']),
                    salary_max=int(vacancy['salary_to']),
                    published_at=vacancy['posted'])
        v.save()
