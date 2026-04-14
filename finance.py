# from agno.agent import Agent
# # 1. OpenAI ki jagah Gemini import karein
# from agno.models.google import Gemini 
# from dotenv import load_dotenv

# load_dotenv()

# def build_agent():
#     return Agent(
#         # 2. OpenAI model ki jagah Gemini setup karein
#         model=Gemini(id="gemini-1.5-flash"),
#         markdown=True,
#         instructions=["You are a helpful and expert travel agent."]
#     )
# # Variable ka naam aap badal sakte hain (optional)
# gemini_agent = build_agent()

# gemini_agent.print_response("My budget is 1L INR, should I travel to Goa or Phuket?")



from agno.agent import Agent
from agno.models.google import Gemini
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.tools.duckduckgo import DuckDuckGoTools

from agno.tools.yfinance import YFinanceTools

load_dotenv()

def build_agent():
    return Agent(
        
        model=Groq(id="qwen/qwen3-32b"),
        tools = [YFinanceTools(), DuckDuckGoTools()],
        markdown=True,
    
        add_datetime_to_context=True,
        description="You are an investment analyst that researches stock prices, analyst recommendations, and stock fundamentals.",
        instructions=["Use Given Tools Whenever Possible Format your response using markdown and use tables to display data where possible."],

       
    )
agent = build_agent()
agent.print_response("Share the NVDA stock price and analyst recommendations", markdown=True)
