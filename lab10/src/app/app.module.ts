import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CompanyCardComponent } from './company-card/company-card.component';
import { VacancyListComponent } from './vacancy-list/vacancy-list.component';
import { VacancyCardComponent } from './vacancy-card/vacancy-card.component';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { VacancyDetailsComponent } from './vacancy-details/vacancy-details.component';
import { CompanyListComponent } from './company-list/company-list.component';

@NgModule({
  declarations: [
    AppComponent,
    CompanyCardComponent,
    VacancyListComponent,
    VacancyCardComponent,
    CompanyDetailsComponent,
    VacancyDetailsComponent,
    CompanyListComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
