from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=64)
    location = models.CharField(max_length=64)
    logo = models.CharField(max_length=64)
    description = models.CharField(max_length=64)
    employee_count = models.IntegerField()

    def __str__(self):
        return f'Компания "{self.name}"'


class Specialty(models.Model):
    code = models.CharField(max_length=16)
    title = models.CharField(max_length=64)
    picture = models.CharField(max_length=64)

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
