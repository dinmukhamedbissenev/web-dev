import { Component } from '@angular/core';
import { Vacancy } from '../vacancy';
import { Input, Output, EventEmitter, OnInit } from '@angular/core';

@Component({
  selector: 'app-vacancy-card',
  templateUrl: './vacancy-card.component.html',
  styleUrls: ['./vacancy-card.component.css']
})
export class VacancyCardComponent {
  @Input() vacancy: Vacancy = {id: 0, name: "", description: "", salary: 0}

}
