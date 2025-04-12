from phi.agent import Agent
# from phi.model.ollama import Ollama
from phi.tools.yfinance import YFinanceTools
from phi.model.groq import Groq

# Define the model to be used by the agent
model = Groq(id="qwen-2.5-32b")  # Replace with your preferred model

# Create the Finance Agent
finance_agent = Agent(
    name="Finance Agent",
    role="Get financial data",
    model=model,
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            company_info=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display data"],
    show_tool_calls=True,
    markdown=True,
)

# Example query to retrieve financial data
# finance_agent.print_response("Summarize analyst recommendations for NVDA", stream=True)
