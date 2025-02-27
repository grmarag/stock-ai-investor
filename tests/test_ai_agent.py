import pandas as pd
from app.ai_agent import AIInvestor

def test_generate_recommendation():
    agent = AIInvestor()
    recommendations = agent.generate_recommendation()
    assert isinstance(recommendations, dict)
    for symbol, data in recommendations.items():
        if isinstance(data, dict):
            assert "current_price" in data
            assert "recommendation" in data
            assert "explanation" in data
            assert data["recommendation"] in ["Buy", "Sell", "Hold", "Error", "No Data"]