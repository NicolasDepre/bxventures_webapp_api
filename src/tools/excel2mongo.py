import pandas as pd
from api.models.models import Solution, Company
import api.database.mongo as dao

filename = "../../BXV Database - Specs test_v29-04-2024.xlsx"

excel = pd.read_excel(filename, header=4).fillna("")
excel.columns = excel.columns.str.lower()
excel.columns = excel.columns.str.replace(' ', '_')
excel.loc[excel["product_name"] == "", 'product_name'] = excel['company_name']


def data2solution(row):
    return Solution(**row)


def data2company(row):
    return Company(**row)


def data2mongodb():
    solution = data2solution(data)
    company = data2company(data)
    solution.company = company.id
    company.solutions.append(solution.id)
    print(solution)
    print(solution.model_dump(by_alias=True))
    dao.insert_solution(solution)
    dao.insert_company(company)
    return solution, company


for index, data in excel.iterrows():
    solution, company = data2mongodb()
