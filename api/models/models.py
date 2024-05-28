from enum import Enum
from pydantic import BaseModel, Field, ConfigDict
from typing import List
from typing_extensions import Annotated
from pydantic.functional_validators import BeforeValidator

PyObjectId = Annotated[str, BeforeValidator(str)]

class MATURITY_STAGE(Enum):
    SEED = "Seed"
    SERIES_A = "Series A"
    SERIES_B = "Series B"
    SERIES_C = "Series C"
    SERIES_D = "Series D"
    SERIES_E = "Series E"
    CORPORATE = "Corporate"
    EXIT_IPO = "Exit – IPO"
    EXIT_ACQUIRED = "Exit - Acquired"


class COMMERCIAL_APPROACH(Enum):
    B2B = "B2B"
    B2C = "B2C"
    B2G = "B2G"


class SECTOR(Enum):
    ENERGY_POWER = "Energy & Power"
    RESOURCES_ENVIRONMENT = "Resources & Environment"
    AGRITECH_FOODTECH = "AgriTech & FoodTech"
    ADVANCED_MATERIALS_CHEMICALS = "Advanced materials & Chemicals"
    ENABLING_TECHNOLOGIES = "Enabling technologies"
    GREEN_TRANSPORTATION_LOGISTICS = "Green transportation & Logistics"


class Solution(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    name: str = Field( description="Product name of the technology")
    country: str = Field( description="Country of the headquarters of the technology")
    location: str = Field( description="City/town of the headquarters of the technology")
    spin_off_from: str = Field(None, description="Name of the university or large corporate if relevant")
    founders: List[str] = Field( description="Names of the founders of the technology")
    private_funding: float = Field(None, description="Amount of funding received from investors in USD")
    public_funding: float = Field(None, description="Amount of funding received from public entities in USD")
    short_description: str = Field( description="Short version of the value proposition description")
    value_proposition: str = Field( description="Long version of the value proposition description")
    commercial_approach: COMMERCIAL_APPROACH = Field( description="Primary commercial approach (B2B, B2C, B2G)")
    un_sdg: List[str] = Field( description="UN Sustainable Development Goals associated with the technology")
    sector: List[SECTOR] = Field( description="Sectors associated with the technology")
    technology_clusters: List[str] = Field(description="Technology clusters linked to sectors")
    technology_tags: List[str] = Field( description="Technology tags for overall search")
    intellectual_property: str = Field(None, description="Short description of intellectual property")
    google_patent_link: str = Field(None, description="Website link to relevant patent")
    environmental_benefits: str = Field(None, description="Short description of environmental benefits")
    article_9_compliance: List[str] = Field( description="Article 9 compliance with sustainable objectives")
    financial_benefits: str = Field(None, description="Short description of financial benefits")
    comments: str = Field(None, description="Space for comments (max 200 characters)")
    image: str = Field(None, description="Image of the technology (standardized size)")
    video: str = Field(None, description="Link to video of the technology (YouTube)")
    model_config = ConfigDict(
        use_enum_values=True,
    )


class Company(BaseModel):
    id: PyObjectId = Field(alias="_id", default=None)
    company_name: str = Field( description="Name of the company (in capital letters)")
    foundation_date: int = Field( description="Year of incorporation of the company")
    country: str = Field( description="Country of the headquarters of the company")
    location: str = Field( description="City/town of the headquarters of the company")
    spin_off_from: str = Field(None, description="Name of the university or large corporate if relevant")
    company_type: str = Field( description="Typology of the company (startup, scale-up, corporate)")
    maturity_stage: MATURITY_STAGE = Field( description="Maturity stage of the technology")
    founders: List[str] = Field( description="Names of the founders of the company")
    number_of_employees: str = Field(None, description="Number of employees as mentioned in LinkedIn")
    private_funding: float = Field(None, description="Amount of funding received from investors in USD")
    public_funding: float = Field(None, description="Amount of funding received from public entities in USD")
    logo: str = Field(None, description="Logo of the company (standardized size)")
    company_website: str = Field(None, description="Link to company website")
    company_linkedin_website: str = Field(None, description="Link to company LinkedIn website")
    comments: str = Field(None, description="Comment of the company")
    model_config = ConfigDict(
        use_enum_values=True,
    )


class SolutionContainer(BaseModel):
    solutions: List[Solution]