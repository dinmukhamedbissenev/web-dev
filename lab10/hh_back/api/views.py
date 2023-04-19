from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import VacancySerializer, CompanySerialier
from .models import Vacancy, Company


@api_view(["GET", "POST", "PUT", "DELETE"])
def company_view(request, company_id=None):
    if request.method == "GET":
        if company_id:
            company = get_object_or_404(Company, id=company_id)
            serializer = CompanySerialier(instance=company)
            return Response(serializer.data, status= status.HTTP_200_OK)
        companies = Company.objects.all()
        serializer = CompanySerialier(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    if request.method == "POST":
        serializer = CompanySerialier(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "PUT":
        if company_id:
            company = get_object_or_404(Company, id=company_id)
            serializer = CompanySerialier(instance=company, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"error": "No id provided"}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        if company_id:
            company = get_object_or_404(Company, id=company_id)
            company.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"error": "No id provided"}, status=status.HTTP_400_BAD_REQUEST)


class VacancyView(APIView):
    def get(self, request, vacancy_id=None):
        if vacancy_id:
            vacancy = get_object_or_404(Vacancy, id=vacancy_id)
            serializer = VacancySerializer(vacancy)
            return Response(serializer.data, status=status.HTTP_200_OK)
        vacancies = Vacancy.objects.all()
        serializer = VacancySerializer(vacancies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = VacancySerializer(data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": "No such company"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        serializer = VacancySerializer(instance=vacancy, data=request.data)
        if serializer.is_valid():
            try:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            except Exception as e:
                return Response({"error": "No such company"}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, vacancy_id):
        vacancy = get_object_or_404(Vacancy, id=vacancy_id)
        vacancy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)