

from agno.agent import Agent
from dotenv import load_dotenv
from agno.models.groq import Groq
from agno.db.sqlite import SqliteDb

load_dotenv()

db = SqliteDb(db_file="agno.db")
db.clear_memories()

def build_agent():
    return Agent(
        db=db,
        model=Groq(id="qwen/qwen3-32b"),
        markdown=True,
        add_history_to_context=True

    )
agent = build_agent()
#agent.print_response("Is it safe to travel to UAE today?")
agent.print_response("What is the capital of Australia?")
agent.print_response("What is the best time to visit it?")