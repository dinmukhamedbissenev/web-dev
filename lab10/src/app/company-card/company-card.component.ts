import { Component } from '@angular/core';
import { Company } from '../company';
import { Input, Output, EventEmitter, OnInit } from '@angular/core';

@Component({
  selector: 'app-company-card',
  templateUrl: './company-card.component.html',
  styleUrls: ['./company-card.component.css']
})
export class CompanyCardComponent implements OnInit{
  @Input() company: Company = <Company>{}

  ngOnInit(): void {
    
  }
}
