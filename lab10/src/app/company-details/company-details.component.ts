import { Component, OnInit} from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { Company } from '../company';
import { CompanyServiceService } from '../company-service.service';

@Component({
  selector: 'app-company-details',
  templateUrl: './company-details.component.html',
  styleUrls: ['./company-details.component.css']
})
export class CompanyDetailsComponent implements OnInit{
  company: Company = <Company>{}

  constructor(private route: ActivatedRoute, private service: CompanyServiceService){}
  ngOnInit(): void {
    this.route.paramMap.subscribe(params => {
      const id = +params.get("id")!
      this.service.getCompany(+id!).subscribe((data) => this.company = data)
    })
  }
}
