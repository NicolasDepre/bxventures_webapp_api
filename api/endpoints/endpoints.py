import fastapi.exceptions
from fastapi import APIRouter

from api.controllers import solutions, company
from api.models.models import Solution, SolutionContainer

router = APIRouter()


@router.get("/solutions",
            response_model=SolutionContainer,
            response_model_by_alias=False)
def get_solutions():
    return SolutionContainer(solutions=solutions.get_all_list_view())


@router.get("/solution/{id}")
def get_solution(id):
    return solutions.get_by_id(id)


@router.get("/companies")
def get_companies():
    return


@router.get("/company/{id}")
def get_company(id):
    return company.get_by_id(id)


@router.post("/solution")
def create_solution(solution: Solution):
    return solutions.insert(solution)
