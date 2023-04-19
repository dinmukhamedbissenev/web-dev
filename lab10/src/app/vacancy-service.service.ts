import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class VacancyServiceService {

  private static apiUrl = "http://127.0.0.1:8000/"

  constructor(private httpClient: HttpClient) { }

  getVacancies(): Observable<Vacancy[]>{
    return this.httpClient.get<Vacancy[]>(`${VacancyServiceService.apiUrl}/vacancies/`)
  }

  getVacancy(vacancyID: number): Observable<Vacancy>{
    return this.httpClient.get<Vacancy>(`${VacancyServiceService.apiUrl}/vacancies/${vacancyID}/`)
  }

  createVacancy(vacancy: Vacancy): Observable<Vacancy>{
    return this.httpClient.post<Vacancy>(`${VacancyServiceService.apiUrl}/vacancies/`, vacancy)
  }

  updateVacancy(vacancy: Vacancy): Observable<Vacancy>{
    return this.httpClient.put<Vacancy>(`${VacancyServiceService.apiUrl}/vacancies/${vacancy.id}/`, vacancy)
  }

  deleteVacancy(vacancy: Vacancy){
    return this.httpClient.delete<Vacancy>(`${VacancyServiceService.apiUrl}/vacancies/${vacancy.id}/`)
  }
}