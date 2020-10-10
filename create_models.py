import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'conf.settings')
django.setup()

from vacancies.models import Vacancy, Specialty, Company
from conf import settings
import random
import data


if __name__ == '__main__':
    for spec in data.specialties:
        s = Specialty(code=spec['code'],
                      title=spec['title'],
                      picture=f'{settings.MEDIA_SPECIALITY_IMAGE_DIR}/specty_{spec["code"]}.png')
        s.save()

    loc = ['Москва', 'Калуга', 'п. Марс', 'Брянск', 'Прага', 'Лос-Анджелес', 'Сухиничи']
    for index, company in enumerate(data.companies, start=1):
        c = Company(name=company['title'],
                    location=random.choice(loc),
                    logo=f'{settings.MEDIA_COMPANY_IMAGE_DIR}/logo{index}.png',
                    description='',
                    employee_count=random.randint(1, 1000))
        c.save()

    skills = ['Python', 'Django', 'Git', 'Linux', 'CSS', 'Excel', 'Photoshop', 'ICQ', 'C++', 'Java', 'C#']
    for vacancy in data.jobs:
        s = Specialty.objects.get(code=vacancy['cat'])
        c = Company.objects.get(name=vacancy['company'])
        v = Vacancy(title=vacancy['title'],
                    specialty=s,
                    company=c,
                    skills=', '.join(random.sample(skills, 4)),
                    description=vacancy['desc'],
                    salary_min=int(vacancy['salary_from']),
                    salary_max=int(vacancy['salary_to']),
                    published_at=vacancy['posted'])
        v.save()
