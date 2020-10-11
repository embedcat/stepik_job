from django.db import models
from django.contrib.auth.models import User
from conf import settings


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.ImageField(upload_to=settings.MEDIA_COMPANY_IMAGE_DIR)
    description = models.CharField(max_length=64)
    employee_count = models.IntegerField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='company')

    def __str__(self):
        return f'Компания "{self.name}"'


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=64)
    picture = models.ImageField(upload_to=settings.MEDIA_SPECIALITY_IMAGE_DIR)

    def __str__(self):
        return f'Специализация {self.title} ({self.code})'


class Vacancy(models.Model):
    title = models.CharField(max_length=64)
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, related_name="vacancies")
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="vacancies")
    skills = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    salary_min = models.IntegerField()
    salary_max = models.IntegerField()
    published_at = models.DateField()

    def __str__(self):
        return f'Вакансия "{self.title}" ({self.specialty}) в {self.company}'


class Application(models.Model):
    written_username = models.CharField(max_length=64)
    written_phone = models.CharField(max_length=64)
    written_cover_letter = models.CharField(max_length=1024)
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE, related_name='application')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='application')
