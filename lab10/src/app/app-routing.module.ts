import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CompanyDetailsComponent } from './company-details/company-details.component';
import { CompanyListComponent } from './company-list/company-list.component';

const routes: Routes = [{path: "companies", component: CompanyListComponent}, 
                        {path: "companies/:id", component: CompanyDetailsComponent},];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
