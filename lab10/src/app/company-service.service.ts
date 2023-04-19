import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Company } from './company';
import { Observable } from 'rxjs';
import { Vacancy } from './vacancy';

@Injectable({
  providedIn: 'root'
})
export class CompanyServiceService {

  private static apiUrl = "http://127.0.0.1:8000"

  constructor(private httpClient: HttpClient) { }

  getCompanies(): Observable<Company[]>{
    console.log('making request...');
    return this.httpClient.get<Company[]>(`${CompanyServiceService.apiUrl}/companies/`);
  }

  getCompany(companyID: number): Observable<Company>{
    return this.httpClient.get<Company>(`${CompanyServiceService.apiUrl}/companies/${companyID}/`);
  }
}
