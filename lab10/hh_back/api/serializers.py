from rest_framework import serializers
from .models import Vacancy, Company

class VacancySerializer(serializers.ModelSerializer):
    company_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Vacancy
        fields = "__all__"

    def create(self, validated_data):
        try:
            company_id = validated_data.pop('company_id')
            company = Company.objects.get(id=company_id)
            vacancy = Vacancy.objects.create(company=company, **validated_data)
            return vacancy
        except Exception as e:
            raise Exception("No such company")


class CompanySerialier(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=20)
    description = serializers.CharField()
    city = serializers.CharField(max_length=20)
    address = serializers.CharField()
    vacancies = VacancySerializer(many=True, read_only=True)

    def create(self, validated_data):
        instance = Company.objects.create(**validated_data)
        return instance

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name')
        instance.description = validated_data.get('description')
        instance.city = validated_data.get('city')
        instance.address = validated_data.get('address')
        instance.save()
        return instance
