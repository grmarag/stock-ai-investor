import json
import pandas as pd
from app.market_data import MarketDataFetcher
from app.config import Config
from openai import OpenAI

class AIInvestor:
    def __init__(self):
        self.fetcher = MarketDataFetcher()
        self.client = OpenAI(api_key=Config.OPENAI_API_KEY)

    def get_recommendation_from_llm(self, symbol: str, data: pd.DataFrame) -> dict:
        """
        Uses the LLM to generate a stock recommendation based on historical data,
        expecting a structured JSON response.
        """
        if data.empty:
            return {
                "recommendation": "No Data",
                "current_price": None,
                "predicted_price": None,
                "explanation": "Insufficient market data."
            }
        
        current_price = data["Close"].iloc[-1]
        avg_price = data["Close"].mean()
        prompt = (
            f"Analyze the following market data for {symbol}:\n"
            f"- Current Price: ${current_price:.2f}\n"
            f"- Average Price over the last month: ${avg_price:.2f}\n\n"
            "Based on current market trends and this data, should an investor buy, sell, or hold this stock? "
            "Return your recommendation as a JSON object with two keys: "
            "'recommendation' (with possible values 'Buy', 'Sell', or 'Hold') and 'explanation' (a brief rationale)."
        )
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a knowledgeable financial advisor."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.0
            )
            response_text = response.choices[0].message.content.strip()

            try:
                parsed_response = json.loads(response_text)
                recommendation = parsed_response.get('recommendation', 'Hold')
                explanation = parsed_response.get('explanation', response_text)
            except json.JSONDecodeError:
                recommendation = "Hold"
                explanation = response_text
            
            return {
                "recommendation": recommendation,
                "current_price": current_price,
                "predicted_price": current_price,
                "explanation": explanation
            }
        except Exception as e:
            return {
                "recommendation": "Error",
                "current_price": current_price,
                "predicted_price": current_price,
                "explanation": f"Error calling LLM: {str(e)}"
            }

    def generate_recommendation(self) -> dict:
        """
        Retrieves market data and uses the LLM to produce recommendations for each stock.
        """
        market_data = self.fetcher.fetch_data()
        recommendations = {}
        for symbol, data in market_data.items():
            rec = self.get_recommendation_from_llm(symbol, data)
            recommendations[symbol] = rec
        return recommendations

    def retrieve_augmented_generation(self, query: str) -> str:
        """
        Combines market insights with external knowledge using the new OpenAI client.
        """
        try:
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are an expert financial advisor."},
                    {"role": "user", "content": query}
                ],
                temperature=0.0
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"Error retrieving information: {str(e)}"