from bson import ObjectId
from pymongo import MongoClient

from api.models.models import Solution, Company

client = MongoClient("mongodb+srv://luster1.ztwaiia.mongodb.net", username="functional", password="jRZJpaUMEchdXtlS")
db = client["bxventures"]
solutions = db.solutions
companies = db.companies


def insert_solution(solution: dict):
    return solutions.insert_one(solution)


def insert_company(company: Company):
    companies.insert_one(company)


def get_solution(filters: dict) -> Solution:
    return solutions.find_one(filters)


def get_company(id: str) -> Company:
    return companies.find_one({"_id": ObjectId(id)})


def get_all_solutions() -> list:
    return solutions.find()