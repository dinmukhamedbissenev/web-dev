import { Vacancy } from "./vacancy"

export interface Company{
    id: number,
    name: String,
    description: String
    city: String,
    address: String,
    vacancies: Vacancy[]
}