from api.database import mongo
from api.models.models import Solution


def insert(solution: Solution):
    solution_dict = {
        k: v for k, v in solution.model_dump(by_alias=True).items() if v is not None
    }
    return mongo.insert_solution(solution_dict)


def get_all():
    return mongo.get_all_solutions()