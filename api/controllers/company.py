from api.database import mongo

def get_all():
    return mongo.get_all_companies()


def get_by_id(company_id: str):
    return mongo.get_company(company_id)