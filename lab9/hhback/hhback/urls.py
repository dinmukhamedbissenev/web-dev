"""hh_back URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from api.views import get_companies, get_company
from api.views import get_company_vacancies, get_vacancies, get_vacancy, get_top_ten

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/companies/', get_companies),
    path('api/companies/<int:id>/', get_company),
    path('api/companies/<int:id>/vacancies/', get_company_vacancies),
    path('api/vacancies/', get_vacancies),
    path('api/vacancies/<int:id>/', get_vacancy),
    path('api/vacancies/top_ten/', get_top_ten)
]