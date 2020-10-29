from django.conf import settings
from django.contrib.auth.models import User
from django.db import migrations, models


DEFAULT_EMAIL = 'dummy@dummy.dummy'
DEFAULT_PASSWORD = '12345678'


def create_company_owners(apps, schema_editor):
    Company = apps.get_model('vacancies', 'Company')
    for company in Company.objects.all():
        owner = User.objects.create_user(
            username=f'{company.name} owner',
            email=DEFAULT_EMAIL,
            password=DEFAULT_PASSWORD)
        print(isinstance(owner, User))  # True
        company.owner_id = owner.id
        company.save()


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vacancies', '0003_auto_20201029_0943'),
    ]

    operations = [
        migrations.RunPython(create_company_owners),
    ]
