from pydantic import BaseModel
from typing import Union

class Recommendation(BaseModel):
    symbol: str
    current_price: float
    predicted_price: float
    recommendation: str
    explanation: str

class RecommendationResponse(BaseModel):
    recommendations: dict[str, Union[str, Recommendation]]