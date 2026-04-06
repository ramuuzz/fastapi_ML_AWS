from pydantic import BaseModel,Field,computed_field,field_validator
from typing import Literal,Annotated
from config.city_tier import tier_1_cities,tier_2_cities

class UserInput(BaseModel):
    age:Annotated[int, Field(...,gt=0, le=120, description="Age of the person in years")]

    weight:Annotated[float, Field(...,gt=0, description="Weight of the person in kg")]
    height:Annotated[float, Field(...,gt=0,le=2.5, description="Height of the person ")]
    income_lpa:Annotated[float, Field(...,ge=0, description="Income of the person in lakhs per annum")]
    smoker:Annotated[bool, Field(..., description="Whether the person is a smoker ")]
    city:Annotated[str, Field(..., description="City of residence")]
    occupation:Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the person")]
    @field_validator('city')
    @classmethod
    def normalize_city(cls, value):
        v=value.strip().title()
        return v        
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height ** 2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi>30:
            return 'high'
        elif self.smoker or self.bmi>27:
            return 'medium'
        else:
            return 'low'
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_aged"
        return "senior"
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        else:
            return 3