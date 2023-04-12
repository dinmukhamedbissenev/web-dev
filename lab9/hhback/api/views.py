from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import Company, Vacancy

# Create your views here.
def get_companies(request):
    return JsonResponse(Company.list_to_json(Company.objects.all()), safe=False)

def get_company(request, id):
    company = Company.objects.filter(id=id).first().to_json()
    return JsonResponse(company)

def get_company_vacancies(request, id):
    vacancies = Vacancy.list_to_json(get_object_or_404(Company, id=id).vacancies)
    return JsonResponse(vacancies, safe=False)

def get_vacancies(request):
    return JsonResponse(Vacancy.list_to_json(Vacancy.objects.all()), safe=False)

def get_vacancy(request, id):
    return JsonResponse(get_object_or_404(Vacancy, id=id).to_json())

def get_top_ten(request):
    return JsonResponse(Vacancy.list_to_json(Vacancy.objects.order_by('-salary').all()[:10]))