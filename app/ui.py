from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from app.ai_agent import AIInvestor

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")

@router.get("/", include_in_schema=False)
async def home(request: Request):
    """
    Renders the homepage with market data and LLM-based AI investment recommendations.
    """
    agent = AIInvestor()
    recommendations = agent.generate_recommendation()
    return templates.TemplateResponse("index.html", {"request": request, "recommendations": recommendations})