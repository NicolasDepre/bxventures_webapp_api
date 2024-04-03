from typing import Union, List
from enum import Enum

from pydantic import BaseModel

class Sector(str, Enum):
    smart_agrigulture_foodtech = "Smart Agriculture and FoodTech"
    clean_energy_power = "Clean Energy and Power"
    advanced_material_chemicals = "Advanced Materials and Chemicals"
    resources_environment = "Resources and Environment"
    green_transportation_logistics = "Green Transportation and Logistics"
    enabling_technologies = "Enabling Technologies"


class Solution(BaseModel):
    tag_line: Union[str, None] = None
    value_proposition: Union[str, None] = None
    sector: Union[Sector, None] = None
    environmental_benefits: Union[str, None] = None
    videos = Union[List[str], None] = None




