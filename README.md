# Stock AI Investor

A Python project that implements state-of-the-art AI agents using LLM-powered recommendations, RAG architectures, and autonomous decision-making. This project acts as a personal investor for the stock market by monitoring real-time data and providing investment recommendations through a beautiful UI.

## Features
- **LLM-Powered Analysis:** Uses OpenAI's model for generating buy/sell recommendations.
- **Real-time Market Data:** Retrieves market data via [yfinance](https://pypi.org/project/yfinance/).
- **Modern UI:** Built with FastAPI, Jinja2 templates, and Bootstrap for a responsive, attractive interface.
- **Containerized:** Dockerfile provided for easy deployment.
- **Tested:** Comprehensive tests with pytest ensure reliability.
- **Dependency Management:** Managed using Poetry.

## Repository Structure

```
stock_ai_investor/
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── config.py
│   ├── market_data.py
│   ├── ai_agent.py
│   ├── models.py
│   ├── ui.py
│   ├── templates/
│   │   ├── base.html
│   │   └── index.html
│   └── static/
│       └── css/
│           └── styles.css
├── tests/
│   ├── __init__.py
│   ├── test_ai_agent.py
│   ├── test_market_data.py
│   └── test_ui.py
├── pyproject.toml
├── README.md
└── Dockerfile
```

## Getting Started

### Prerequisites
- **Docker:** For containerized deployment.
- **Python 3.9+:** Ensure you have a compatible Python version.
- **Poetry:** For dependency management.

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/stock_ai_investor.git
   cd stock_ai_investor
   ```

2. **Install dependencies with Poetry:**
   ```bash
   poetry install
   ```

3. **Set your OpenAI API key:**
   Create a `.env` file and add your OpenAI API key:
   ```env
   OPENAI_API_KEY=your-api-key-here
   ```

4. **Run the application:**
   ```bash
   poetry run uvicorn app.main:app --reload
   ```
   Open [http://localhost:8000](http://localhost:8000) in your browser to view the UI.

### Running Tests
Execute tests using:
```bash
poetry run pytest
```

### Docker Deployment

1. **Build the Docker image:**
   ```bash
   docker build -t stock-ai-investor .
   ```

2. **Run the Docker container:**
   ```bash
   docker run -p 8000:8000 stock-ai-investor
   ```

## License
This project is licensed under the [MIT License](LICENSE).